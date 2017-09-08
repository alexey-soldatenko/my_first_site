from django.contrib import admin
from articles.models import Articles, Part, Comments

class PartAdmin(admin.ModelAdmin):
	list_display = ['name_part']

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ['title', 'part', 'date_publicate']
	ordering = ['part', 'title']

class CommentsAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'article_name', 'context', 'date']

# Register your models here.
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Comments, CommentsAdmin)