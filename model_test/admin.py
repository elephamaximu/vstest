from django.contrib import admin
from . models import Repoter, Article, Publication, Restaurant, Waiter, Place
# Register your models here.

admin.site.register(Repoter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Place)