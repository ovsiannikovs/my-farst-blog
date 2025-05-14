from django.contrib import admin
from .models import Post
from .models import TechnicalProposal

@admin.register(TechnicalProposal)
class TechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_of_creation']


admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'design_product', 'author', 'date_of_creation')  
