from django.contrib import admin
from .forms import *
from django_summernote.admin import SummernoteModelAdmin
from .models import Articles

class ArticlesAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('full', 'decision')



class BlogAdmin(admin.ModelAdmin):
    summernote_fields = ('title', 'body')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Articles, ArticlesAdmin)






