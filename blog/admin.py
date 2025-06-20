from django.contrib import admin
from .models import Post
from .models import TechnicalProposal
from .models import ListTechnicalProposal
from .models import GeneralDrawingProduct
from .models import ElectronicModelProduct
from .models import GeneralElectricalDiagram
from .models import SoftwareProduct
from .models import GeneralDrawingUnit
from .models import ElectronicModelUnit
from .models import DrawingPartUnit
from .models import ElectronicModelPartUnit
from .models import DrawingPartProduct 
from .models import ElectronicModelPartProduct
from .models import ReportTechnicalProposal
from .models import AddReportTechnicalProposal
from .models import ProtocolTechnicalProposal





@admin.register(TechnicalProposal)
class TechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_of_creation']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'design_product', 'author', 'date_of_creation')  

@admin.register(ListTechnicalProposal)
class ListTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'desig_document', 'status', 'date_of_creation']
    search_fields = ['name', 'desig_document']

@admin.register(GeneralDrawingProduct)
class GeneralDrawingProductAdmin(admin.ModelAdmin):
    list_display = (
        'name','desig_document','category','author','date_of_creation','status','version',
    )
    search_fields = ('name', 'desig_document')
    list_filter = ('category', 'status', 'trl', 'litera')

@admin.register(ElectronicModelProduct)
class ElectronicModelProductAdmin(admin.ModelAdmin):
    list_display = (
        'name','desig_document','author','date_of_creation','status','version','trl',
    )
    search_fields = ('name', 'desig_document')
    list_filter = ('status', 'trl', 'category', 'develop_org')

@admin.register(GeneralElectricalDiagram)
class GeneralElectricalDiagramAdmin(admin.ModelAdmin):
    list_display = (
        'name','desig_document','author','date_of_creation','status','version',
    )
    search_fields = ('name', 'desig_document', 'author__username')
    list_filter = ('status', 'trl', 'develop_org', 'language')    

@admin.register(SoftwareProduct)
class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'desig_document', 'status', 'version', 'date_of_creation')
    search_fields = ('name', 'desig_document', 'status')
    list_filter = ('status', 'category', 'trl', 'version')    

@admin.register(GeneralDrawingUnit)
class GeneralDrawingUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document', 'status', 'version', 'technical_proposal')    

@admin.register(ElectronicModelUnit)
class ElectronicModelUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document', 'status', 'version', 'technical_proposal')

@admin.register(DrawingPartUnit)
class DrawingPartUnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desig_document',
        'category',
        'status',
        'version',
        'date_of_creation',
        'last_editor',
        'develop_org',
    )
    list_filter = ('status', 'category', 'trl', 'develop_org')
    search_fields = ('name', 'desig_document', 'author__username', 'last_editor__username')
    readonly_fields = ('date_of_creation', 'date_of_change', 'version_diff', 'litera', 'trl')
    ordering = ('-date_of_creation',)

    fieldsets = (
        (None, {
            'fields': (
                'name', 'category', 'desig_document', 'technical_proposal',
                'file', 'application', 'info_format', 'primary_use', 'change_number'
            )
        }),
        ('Состояние и управление', {
            'fields': (
                'status', 'priority', 'approval_cycle', 'version', 'version_diff',
                'litera', 'trl', 'validity_date', 'subscribers', 'related_documents'
            )
        }),
        ('Ответственные', {
            'fields': (
                'author', 'last_editor', 'current_responsible', 'develop_org', 'language'
            )
        }),
        ('Служебные поля', {
            'fields': (
                'date_of_creation', 'date_of_change', 'pattern'
            )
        }),
    )  

@admin.register(ElectronicModelPartUnit)
class ElectronicModelPartUnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desig_document',
        'category',
        'status',
        'version',
        'trl',
        'date_of_creation',
        'last_editor',
    )
    search_fields = ('name', 'desig_document', 'category')
    list_filter = ('status', 'trl', 'category', 'develop_org')
    readonly_fields = ('date_of_creation', 'date_of_change')

    fieldsets = (
        (None, {
            'fields': (
                'category', 'name', 'desig_document', 'info_format',
                'primary_use', 'change_number', 'file', 'application',
                'technical_proposal', 'pattern', 'version', 'version_diff',
                'approval_cycle', 'litera', 'trl', 'validity_date',
                'subscribers', 'related_documents', 'develop_org', 'language'
            )
        }),
        ('Ответственные', {
            'fields': ('author', 'last_editor', 'current_responsible')
        }),
        ('Статус', {
            'fields': ('status', 'priority')
        }),
        ('Временные метки', {
            'fields': ('date_of_creation', 'date_of_change')
        }),
    )   

@admin.register(DrawingPartProduct)
class DrawingPartProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'desig_document',
        'name',
        'category',
        'status',
        'version',
        'trl',
        'author',
        'current_responsible',
        'date_of_creation',
        'date_of_change',
    )
    list_filter = ('category', 'status', 'trl', 'date_of_creation')
    search_fields = ('name', 'desig_document', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_creation', 'date_of_change', 'author', 'last_editor')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change) 

@admin.register(ElectronicModelPartProduct)
class ElectronicModelPartProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'desig_document', 'name', 'category',
        'status', 'version', 'trl', 'author',
        'current_responsible', 'date_of_creation', 'date_of_change'
    )
    list_filter = ('category', 'status', 'trl', 'date_of_creation')
    search_fields = ('desig_document', 'name', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_creation', 'date_of_change', 'author', 'last_editor')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)          

@admin.register(ReportTechnicalProposal)
class ReportTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'desig_document', 'category', 'status', 'version',
        'trl', 'author', 'current_responsible', 'date_of_creation'
    )
    list_filter = ('category', 'status', 'trl', 'date_of_creation')
    search_fields = ('name', 'desig_document', 'author__username')
    readonly_fields = (
        'date_of_creation', 'date_of_change', 'author', 'last_editor'
    )

@admin.register(AddReportTechnicalProposal)
class AddReportTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desig_document',
        'category',
        'status',
        'version',
        'trl',
        'author',
        'current_responsible',
        'date_of_creation',
        'date_of_change',
    )
    list_filter = ('category', 'status', 'trl', 'date_of_creation')
    search_fields = ('name', 'desig_document', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_creation', 'date_of_change', 'author', 'last_editor')
    fieldsets = (
        (None, {
            'fields': (
                'category',
                'name',
                'desig_document',
                'info_format',
                'primary_use',
                'file',
                'application',
                'status',
                'priority',
                'approval_cycle',
                'version',
                'version_diff',
                'litera',
                'trl',
                'validity_date',
                'subscribers',
                'related_documents',
                'pattern',
                'develop_org',
                'language',
                'permission',
                'access_level',
                'author',
                'last_editor',
                'current_responsible',
                'date_of_creation',
                'date_of_change',
            )
        }),
    )   

@admin.register(ProtocolTechnicalProposal)
class ProtocolTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'desig_document', 'category',
        'status', 'version', 'trl',
        'author', 'current_responsible',
        'date_of_creation', 'date_of_change'
    )
    list_filter = ('status', 'category', 'trl', 'date_of_creation')
    search_fields = ('name', 'desig_document', 'author__username', 'current_responsible__username')
    readonly_fields = ('id', 'date_of_creation', 'date_of_change', 'author', 'last_editor')

    def save_model(self, request, obj, form, change):
        """Автоматически проставляем автора и редактора"""
        if not obj.pk:
            obj.author = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)     