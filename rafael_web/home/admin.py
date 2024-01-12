from django.contrib import admin

from home.models import Category, Comment, Post

# Models from the navbar app
from home.models import NavBar, NavBarToggle

# Register your models here.
admin.site.register(NavBar)
admin.site.register(NavBarToggle)
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
