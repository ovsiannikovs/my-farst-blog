from django.contrib import admin
from .models import TechnicalProposal
from .models import Post

# Правильная регистрация TechnicalProposal
@admin.register(TechnicalProposal)
class TechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_of_creation']

# Правильная регистрация Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'design_product', 'author', 'date_of_creation')
