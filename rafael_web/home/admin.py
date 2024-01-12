from django.contrib import admin

from home.models import Category, Comment, Post

# Models from the navbar app
from home.models import NavBar, NavBarToggle
# Models from the testimonials section
from home.models import Testimonial

# Register your models here.
admin.site.register(NavBar)
admin.site.register(NavBarToggle)

# Models from the testimonials section
admin.site.register(Testimonial)

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
