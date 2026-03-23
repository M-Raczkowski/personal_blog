
from django.contrib import admin
from blog.models import Category, Post, Photo, Author

class CategoryAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Photo)
admin.site.register(Author, AuthorAdmin)
