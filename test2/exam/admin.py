from exam.models import *
from django.contrib import admin


class Admin_Zombie(admin.ModelAdmin):
	list_display = ('name','cementery',)


class Admin_Tweet(admin.ModelAdmin):
	list_display = ('status','zombie',)

admin.site.register(Zombie, Admin_Zombie,)
admin.site.register(Tweet, Admin_Tweet,)
