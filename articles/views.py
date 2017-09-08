from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles.models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import CommentForm
from articles.models import Comments


	

# Create your views here.

def display_stat(request, part_name, name_article):
	''' Отображение страницы со статьёй, где part_name - название раздела, name_article - название самой статьи'''

	html = part_name+name_article+'.html'
	# проверка аутентификации пользователя
	if request.user.is_authenticated():
		user = request.user.username
		anonymous = False
	else:
		user = 'Anonymous'
		anonymous = True
	#комментарий может оставлять только аутентифицированный пользователь
	if request.method == 'POST':
		if anonymous:
			return redirect('/login')
		else:
			# получение комментария
			if request.POST['comment']:
				com = request.POST['comment']
				#сщхранение комментария в базе данных
				comment = Comments(user_name=user, article_name=name_article, context=request.POST.get('comment'))
				comment.save()
				#переадресация на ту же страницу
				return redirect('articles.views.display_stat', part_name = part_name, name_article = name_article)
	# если есть комментарии к данной статье - отобразить их
	if Comments.objects.filter(article_name=name_article):
		comments = Comments.objects.filter(article_name=name_article)
	else:
		comments = ''

	return render(request, html, {'user': str(user), 'anonymous': anonymous, 'comments': comments})
	

def display_articles(request, page=1):
	'''Вывод списка статей при помощи paginator'''

	articles_list = Articles.objects.all()
	paginator = Paginator(articles_list, 5)

	page_num = page
	try:
		articles = paginator.page(page_num)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	if request.user.is_authenticated():
		user = request.user.username
		anonymous = False
	else:
		user = 'Anonymous'
		anonymous = True

	return render(request, 'articles.html', {'articles':articles, 'user': str(user), 'anonymous': anonymous})


def search_word(request):
	'''Поиск слова в содержании каждой статьи '''
	articles = Articles.objects.raw('Select * from articles_articles')
	find_word = request.GET['word']
	#создаем список слов из строки запроса
	list_word = find_word.split(' ')
	#выходной список словарей, с параметрами каждой совпадающей статьи
	out_list = []
	for article in articles:
		context = article.context
		for word in list_word:
			articles_dict = {}
			if context.find(word) != -1:
				articles_dict["title"] = article.title
				articles_dict["part"] = article.part
				articles_dict["url_name"] = article.url_name
				out_list.append(articles_dict)
				del articles_dict
				
	if request.user.is_authenticated():
		user = request.user.username
		anonymous = False
	else:
		user = 'Anonymous'
		anonymous = True
	return render(request, 'search_result.html', {'list_articles': out_list, 'user': str(user), 'anonymous': anonymous})

