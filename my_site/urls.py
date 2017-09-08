from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from articles.views import display_articles

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^my_secure_admin/', include(admin.site.urls)),

    url(r'^$', 'views.display_template', {'html':'home.html'}),
    url(r'^about$', 'views.display_template', {'html':'about_me.html'}),
    url(r'^other_sources$', 'views.display_template', {'html':'other_sources.html'}),

    url(r'^(?P<part_name>python_tutorial/|django_tutorial/)', include('articles.urls')),

    url(r'^articles/(?P<page>\d+)?$', display_articles), 

    url(r'^pdf$', 'views.display_PDF'),
    
    url(r'^login$', 'views.login_user'),
    url(r'^registration$','views.registration_user'),
    url(r'^logout$', 'views.logout_user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'views.activate', name='activate'),
    url(r'^search/$', 'articles.views.search_word'),
   
]
