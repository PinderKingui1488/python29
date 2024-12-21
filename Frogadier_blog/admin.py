from django.contrib import admin

from Frogadier_blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "views_counter")
    search_fields = ("name", "views_counter")