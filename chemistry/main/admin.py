from django.contrib import admin
from .forms import *
from django_summernote.admin import SummernoteModelAdmin
from .models import Massive

class MassiveAdmin(SummernoteModelAdmin):
    summernote_fields = ('mean')


admin.site.register(Massive, MassiveAdmin)



