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
from crm.models import Notifications, Customer, Decision_maker, Deal, Product, Deal_stage, Call, Letter
from .models import TechTask
from .models import (
    OKRTask,
    Template,
    ReworkTask,
    WorkPlan,
)




@admin.register(TechnicalProposal)
class TechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_of_creation']
    readonly_fields = ('date_of_creation', 'date_of_change')

class ListTechnicalProposalInline(admin.TabularInline):
    model = ListTechnicalProposal
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_product', 'author', 'date_of_creation', 'date_of_change')
    inlines = [ListTechnicalProposalInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.post = form.instance
            if not instance.name:
                instance.name = instance.post.name
            instance.save()
        formset.save_m2m()

@admin.register(ListTechnicalProposal)
class ListTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'desig_document', 'status', 'date_of_creation']
    search_fields = ['name', 'desig_document']


    def save_model(self, request, obj, form, change):
        if obj.post and not obj.name:
            obj.name = obj.post.name
        super().save_model(request, obj, form, change)

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
    list_display = ('name', 'desig_document', 'status', 'version')    

@admin.register(ElectronicModelUnit)
class ElectronicModelUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document', 'status', 'version')

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
                'name', 'category', 'desig_document',
                'info_format', 'primary_use', 'change_number'
            )
        }),
        ('Состояние и управление', {
            'fields': (
                'status', 'priority', 'version', 'version_diff',
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
                'primary_use', 'change_number',
                'pattern', 'version', 'version_diff',
                'litera', 'trl', 'validity_date',
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
        'id', 'name', 'category', 'status', 'version',
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
    search_fields = ('name', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_creation', 'date_of_change', 'author', 'last_editor')
    fieldsets = (
        (None, {
            'fields': (
                'category',
                'name',
                'info_format',
                'status',
                'version',
                'version_diff',
                'litera',
                'trl',
                'validity_date',
                'subscribers',
                'related_documents',
                'develop_org',
                'language',
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

class RevenueRangeFilter(admin.SimpleListFilter):
    title = 'Выручка'
    parameter_name = 'revenue_range'

    def lookups(self, request, model_admin):
        return [
            ('<100', 'до 100 млрд'),
            ('100-500', '100–500 млрд'),
            ('>500', 'более 500 млрд'),
        ]

    def queryset(self, request, queryset):
        def parse(value):
            try:
                return float(value.replace(',', '.'))
            except:
                return 0

        if self.value() == '<100':
            return queryset.filter(revenue_for_last_year__lt='100')
        elif self.value() == '100-500':
            return queryset.filter(
                revenue_for_last_year__gte='100',
                revenue_for_last_year__lte='500'
            )
        elif self.value() == '>500':
            return queryset.filter(revenue_for_last_year__gt='500')
        return queryset


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name_of_company', 'revenue_for_last_year', 'length_of_electrical_network_km')
    list_filter = ('name_of_company', 'revenue_for_last_year')  # Фильтры в правой части
    list_filter = (RevenueRangeFilter,)
    search_fields = ('name_of_company', 'address')  # Поиск по этим полям


class Decision_makerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city_of_location', 'function', 'customer')
    list_filter = ('city_of_location', 'function', 'customer')
    search_fields = ('full_name', 'phone_number', 'email')


class DealAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_date', 'status', 'deal_amount')
    list_filter = ('customer', 'start_date', 'customer')
    search_fields = ('customer__name_of_company', 'description')
    date_hierarchy = 'start_date'  # Иерархия по дате


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_of_product', 'end_customer_price')
    list_filter = ('name_of_product',)
    search_fields = ('name_of_product', 'description')


class Deal_stageAdmin(admin.ModelAdmin):
    list_display = ('deal', 'start_date_step', 'status')
    list_filter = ('status', 'deal')
    search_fields = ('deal__customer__name_of_company', 'description_of_task_at_stage')


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('customer', 'decision_maker', 'planned_date', 'responsible', 'deal')
    search_fields = ('call_goal', 'call_result')
    list_filter = ('planned_date',)
    date_hierarchy = 'planned_date'


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('incoming_number', 'customer', 'planned_date', 'responsible', 'deal')
    search_fields = ('incoming_number', 'responsible_person_from_customer')
    list_filter = ('planned_date',)
    date_hierarchy = 'planned_date'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Decision_maker, Decision_makerAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Deal_stage, Deal_stageAdmin)
admin.site.register(Notifications) 

@admin.register(OKRTask)
class OKRTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'status', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'version')
    list_filter = ('status', 'priority', 'category')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'template_type', 'status', 'created_by', 'created_at')
    search_fields = ('name', 'template_type')
    list_filter = ('status', 'access_level')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(ReworkTask)
class ReworkTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'status', 'created_by', 'created_at')
    search_fields = ('name', 'version')
    list_filter = ('status', 'priority',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(WorkPlan)
class WorkPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'status', 'created_by', 'created_at')
    search_fields = ('name', 'version')
    list_filter = ('status', 'priority',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(TechTask)
class TechTaskAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'version', 'status', 'created_by', 'created_at', 'updated_at', 'editor'
    )
    search_fields = ('name', 'version')
    list_filter = ('status', 'access_level')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'change_description')

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'name', 'version', 'status',
            )
        }),
        ('Файловые и связные поля', {
            'fields': (
                'template', 'okr_task', 'rework_task', 'work_plan'
            )
        }),
        ('Служебная информация', {
            'fields': (
                'created_by', 'created_at', 'updated_by', 'updated_at', 'editor',
                'change_description', 'permission_level', 'access_level'
            )
        }),
    )