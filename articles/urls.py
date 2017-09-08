from django.conf.urls import include, url
from articles.views import display_stat

urlpatterns = [

	url(r'^(?P<name_article>\w+)$', display_stat),

]