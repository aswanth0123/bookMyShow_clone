from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(movie)
admin.site.register(member)
admin.site.register(language)
admin.site.register(movie_members)