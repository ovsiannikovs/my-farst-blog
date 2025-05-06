from django.contrib import admin
from .models import Post

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_product', 'author', 'date_of_creation')  