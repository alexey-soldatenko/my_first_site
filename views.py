from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from forms import LoginForm, RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from tokens import account_activation_token
from django.core.mail import EmailMessage

def display_PDF(request):
	'''Вывод pdf-файла '''
	with open('templates/djangobook1.pdf', 'rb') as pdf:
		pdf_data = pdf.read()

	return HttpResponse(pdf_data, content_type='application/pdf')

def login_user(request):
	'''Аутентификация пользователя, вход в систему'''
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data["name"]
			password = form.cleaned_data["password"]
			user = authenticate(username=user_name, password=password)
			if user is not None:
			#функция login() выполняется только после аутентификации
				login(request, user)
				return redirect( '/')
			else:
				error = 'Неверно введено имя или пароль.'
				return render(request, 'auth/sign_up.html', {'form':form, 'error': error})			
	else:
		form = LoginForm()
	return render(request, 'auth/sign_up.html', {'form':form})

def registration_user(request):
	'''Регистрация пользователя и отправка сообщения на почту с ссылкой активации '''
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			#получаем "чистые" данные пользователя
			if form.cleaned_data['password1'] == form.cleaned_data['password1']:
				user_name = form.cleaned_data['name']
				e_mail = form.cleaned_data['e_mail']
				password = form.cleaned_data['password1']
				#создаём пользователя и сохраняем его как неактивного
				user = User.objects.create_user(user_name, e_mail, password)
				user.is_active = False
				user.save()
				current_site = get_current_site(request)
				mail_subject = 'Activate your account'
				#сообщение с закодированной ссылкой
				message = render_to_string('acc_active_email.html', 
					{
					'user':user,
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token':account_activation_token.make_token(user)
					})
				to_email = e_mail
				email = EmailMessage(
					mail_subject, message, to=[to_email])
				#отправляем сообщение для подтверждения почты
				email.send()
				return HttpResponse('Please confirm your email address to comlete the registration')
	else:
		form = RegisterForm()
	return render(request, 'auth/registration.html', {'form': form})
	

def logout_user(request):
	'''Выход пользователя из системы '''
	if request.user.is_authenticated():
		logout(request)
	return redirect('/') 



def activate(request, uidb64, token):
	'''Проверка активизационной ссылки, активация пользователя '''
	try:
		#декодируем значение id пользователя из адреса
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
		#если пользователь найден по id и токен совпадает делаем пользователя активным 
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		#аутентификация и вход
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request, user)
		return HttpResponse('Thanks for your confirm')
	else:
		return HttpResponse('Activate link is invalid')






def display_template(request, html):
	'''Отображение простой страницы '''
	if request.user.is_authenticated():
		user = request.user.username
		anonymous = False
	else:
		user = 'Anonymous'
		anonymous = True

	return render(request, html, {'user': str(user), 'anonymous': anonymous})
