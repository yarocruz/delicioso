from django.contrib import admin
from .models import Bookmark, User, Url, Tag

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(User)
admin.site.register(Url)
admin.site.register(Tag)
