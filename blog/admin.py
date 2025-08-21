from django.contrib import admin, messages
from django.urls import reverse, path
from django.utils.html import format_html
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
from crm.models import Notifications, Customer, Decision_maker, Deal, Product, Deal_stage, Call, Letter, Company_branch, Meeting
from .models import TechnicalAssignment, TaskForDesignWork, RevisionTask, WorkAssignment
from .forms import WorkAssignmentForm
from .models import WorkAssignmentDeadlineChange
from .admin_forms import RescheduleAdminForm
from .services import WorkAssignmentService



@admin.register(TechnicalProposal)
class TechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'date_of_creation']
    readonly_fields = ('date_of_creation', 'date_of_change')

class ListTechnicalProposalInline(admin.TabularInline):
    model = ListTechnicalProposal
    extra = 1
    can_delete = True

    def has_add_permission(self, request, obj=None):
        if obj and ListTechnicalProposal.objects.filter(post=obj).count() >= 1:
            return False
        return True

class TechnicalAssignmentInline(admin.TabularInline):  # или StackedInline
    model = TechnicalAssignment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document_post', 'author', 'date_of_creation', 'date_of_change', 'technical_assignments_count',
        'open_tech_assignments_link',
        'add_tech_assignment_link',)
    search_fields = ('name',)
    readonly_fields = ('date_of_change',)
    inlines = [ListTechnicalProposalInline, TechnicalAssignmentInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.post = form.instance

            # Если name пустое или только пробелы — взять из головной модели
            if not instance.name or not instance.name.strip():
                instance.name = instance.post.name


            instance.save()
        formset.save_m2m()
    def technical_assignments_count(self, obj):
        return obj.technical_assignments.count()
    technical_assignments_count.short_description = 'ТЗ (шт.)'

    def open_tech_assignments_link(self, obj):
        url = reverse('admin:blog_technicalassignment_changelist') + f'?post__id__exact={obj.pk}'
        return format_html('<a class="button" href="{}">📂 Открыть ТЗ</a>', url)
    open_tech_assignments_link.short_description = 'Тех. задания'

    def add_tech_assignment_link(self, obj):
        url = reverse('admin:blog_technicalassignment_add') + f'?post={obj.pk}'
        return format_html('<a class="button" href="{}">➕ Новое ТЗ</a>', url)
    add_tech_assignment_link.short_description = 'Создать ТЗ'

try:
    admin.site.unregister(Post)
except admin.sites.NotRegistered:
    pass
admin.site.register(Post, PostAdmin)

@admin.register(ListTechnicalProposal)
class ListTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'desig_document_list_technical_proposal', 'status', 'date_of_creation']
    search_fields = ['name', 'desig_document_list_technical_proposal']
    readonly_fields = ('date_of_change',)


    def save_model(self, request, obj, form, change):
        if obj.post and not obj.name:
            obj.name = obj.post.name
        super().save_model(request, obj, form, change)

@admin.register(GeneralDrawingProduct)
class GeneralDrawingProductAdmin(admin.ModelAdmin):
    list_display = (
        'name','category','author','date_of_creation','status','version',
    )
    search_fields = ('name',)
    list_filter = ('category', 'status', 'trl', 'litera')
    readonly_fields = ('date_of_change',)

@admin.register(ElectronicModelProduct)
class ElectronicModelProductAdmin(admin.ModelAdmin):
    list_display = (
        'name','desig_document_electronic_model_product','author','date_of_creation','status','version','trl',
    )
    search_fields = ('name', 'desig_document_electronic_model_product')
    list_filter = ('status', 'trl', 'category', 'develop_org')
    readonly_fields = ('date_of_change', 'info_format')

@admin.register(GeneralElectricalDiagram)
class GeneralElectricalDiagramAdmin(admin.ModelAdmin):
    list_display = (
        'name','desig_document','author','date_of_creation','status','version',
    )
    search_fields = ('name', 'desig_document', 'author__username')
    list_filter = ('status', 'trl', 'develop_org', 'language')
    readonly_fields = ('date_of_change',)

@admin.register(SoftwareProduct)
class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'desig_document_software_product', 'status', 'version', 'date_of_creation')
    search_fields = ('name', 'desig_document_software_product', 'status')
    list_filter = ('status', 'category', 'version')
    readonly_fields = ('date_of_change',)

@admin.register(GeneralDrawingUnit)
class GeneralDrawingUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document_general_drawing_unit', 'status', 'version')
    readonly_fields = ('date_of_change',)

@admin.register(ElectronicModelUnit)
class ElectronicModelUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'desig_document_electronic_model_unit', 'status', 'version')
    readonly_fields = ('date_of_change',)

@admin.register(DrawingPartUnit)
class DrawingPartUnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'status',
        'version',
        'date_of_creation',
        'last_editor',
        'develop_org',
    )
    list_filter = ('status', 'category', 'trl', 'develop_org')
    search_fields = ('name', 'author__username', 'last_editor__username')
    ordering = ('-date_of_creation',)
    readonly_fields = ('date_of_change',)

    fieldsets = (
        (None, {
            'fields': (
                'name', 'category',
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
        'desig_document_electronic_model_part_unit',
        'category',
        'status',
        'version',
        'trl',
        'date_of_creation',
        'last_editor',
    )
    search_fields = ('name', 'desig_document_electronic_model_part_unit', 'category')
    list_filter = ('status', 'trl', 'category', 'develop_org')
    readonly_fields = ('date_of_change', 'info_format')

    fieldsets = (
        (None, {
            'fields': (
                'category', 'name', 'desig_document_electronic_model_part_unit', 'info_format',
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
        'desig_document_drawing_part_product',
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
    search_fields = ('name', 'desig_document_drawing_part_product', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_change',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)

@admin.register(ElectronicModelPartProduct)
class ElectronicModelPartProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'desig_document_electronic_model_part_product', 'name', 'category',
        'status', 'version', 'trl', 'author',
        'current_responsible', 'date_of_creation', 'date_of_change'
    )
    list_filter = ('category', 'status', 'trl', 'date_of_creation')
    search_fields = ('desig_document_electronic_model_part_product', 'name', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_change', 'info_format')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)

@admin.register(ReportTechnicalProposal)
class ReportTechnicalProposalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'category', 'status', 'version',
        'author', 'current_responsible', 'date_of_creation'
    )
    list_filter = ('category', 'status', 'date_of_creation')
    search_fields = ('name', 'desig_document_report_technical_proposal', 'author__username')
    readonly_fields = ('date_of_change',)

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
    readonly_fields = ('date_of_change',)
    search_fields = ('name', 'author__username', 'current_responsible__username')
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
        'id', 'name', 'desig_document_protocol_technical_proporsal', 'category',
        'status', 'version',
        'author', 'current_responsible',
        'date_of_creation', 'date_of_change'
    )
    list_filter = ('status', 'category', 'date_of_creation')
    search_fields = ('name', 'desig_document_protocol_technical_proporsal', 'author__username', 'current_responsible__username')
    readonly_fields = ('date_of_change',)

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


@admin.register(Company_branch)
class Company_branchAdmin(admin.ModelAdmin):
    list_display = ('name_of_company', 'revenue_for_last_year', 'length_of_electrical_network_km')
    list_filter = ('name_of_company', 'revenue_for_last_year')  # Фильтры в правой части
    list_filter = (RevenueRangeFilter,)
    search_fields = ('name_of_company', 'address')  # Поиск по этим полям


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'decision_maker', 'responsible_user', 'planned_date')
    list_filter = ('planned_date', 'customer', 'decision_maker', 'responsible_user')
    search_fields = ('goal_description', 'result_description')
    ordering = ('-planned_date',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Decision_maker, Decision_makerAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Deal_stage, Deal_stageAdmin)
admin.site.register(Notifications)


class TaskForDesignWorkInline(admin.TabularInline):
    model = TaskForDesignWork
    extra = 1

class RevisionTaskInline(admin.TabularInline):
    model = RevisionTask
    extra = 1

class WorkAssignmentInline(admin.TabularInline):
    model = WorkAssignment
    extra = 0
    fields = ('name', 'deadline', 'result')
    readonly_fields = ('name',)

    def get_extra_buttons(self, obj):
        if obj and obj.id:
            url = reverse('admin:blog_workassignment_add') + f'?technical_assignment={obj.id}'
            return format_html('<a class="button" href="{}">➕ Добавить рабочее задание</a>', url)
        return ''

    def get_fieldsets(self, request, obj=None):
        """Добавляем кнопку прямо в заголовок инлайна"""
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.id:
            return [(f"Рабочие задания {self.get_extra_buttons(obj)}", {'fields': self.fields})]
        return fieldsets

@admin.register(TaskForDesignWork)
class TaskForDesignWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'date_of_creation', 'status', 'version', 'technical_assignment', 'open_task_link', 'add_task_link')
    search_fields = ('name', 'author__username', 'current_responsible__username')
    list_filter = ('status', 'priority', 'language', 'technical_assignment')
    readonly_fields = ('date_of_creation', 'date_of_change')
    search_fields = ('name',)

    def open_task_link(self, obj):
        url = reverse('admin:blog_taskfordesignwork_changelist') + f'?technical_assignment__id__exact={obj.technical_assignment_id}'
        return format_html('<a class="button" href="{}">Открыть ПЗ</a>', url)
    open_task_link.short_description = 'Список ПЗ'

    def add_task_link(self, obj):
        url = reverse('admin:blog_taskfordesignwork_add') + f'?technical_assignment={obj.technical_assignment_id}'
        return format_html('<a class="button" href="{}">Новое ПЗ</a>', url)
    add_task_link.short_description = 'Создать ПЗ'

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        ta_id = request.GET.get('technical_assignment')
        if ta_id:
            initial['technical_assignment'] = ta_id
        return initial

    class Media:
        css = {
            'all': ('admin/admin_hscroll.css',)  # тот же CSS со скроллом
        }


@admin.register(RevisionTask)
class RevisionTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'technical_assignment', 'date_of_creation', 'status', 'version')
    search_fields = ('name', 'author__username', 'current_responsible__username', 'technical_assignment__name')
    list_filter = ('status', 'priority', 'language', 'technical_assignment',)
    readonly_fields = ('date_of_creation', 'date_of_change')

    autocomplete_fields = ['technical_assignment']


class DeadlineChangeInline(admin.TabularInline):
    model = WorkAssignmentDeadlineChange
    extra = 0
    can_delete = False
    readonly_fields = (
        "old_target_deadline","old_hard_deadline","old_time_window_start","old_time_window_end",
        "new_target_deadline","new_hard_deadline","new_time_window_start","new_time_window_end",
        "reason","changed_by","changed_at",
    )
    show_change_link = False

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        tech_id = request.GET.get('technical_assignment')
        if tech_id:
            initial['technical_assignment'] = tech_id
        return initial

@admin.register(WorkAssignment)
class WorkAssignmentAdmin(admin.ModelAdmin):
    #form = WorkAssignmentForm

    list_display = (
        'name', 'category', 'author',
        'effective_deadline_readonly',  # новый столбец
        'overdue_flag',                 # новый столбец
        'result', 'version',
        'target_deadline', 'hard_deadline',
        'control_status', 'control_date',
        'deadline_version', 'reschedule_count',  # служебные
    )
    search_fields = ('name','author__username','current_responsible__username')
    list_filter = ('result','control_status')

    readonly_fields = ('date_of_creation','date_of_change',
                       'effective_deadline_readonly','deadline_version','reschedule_count')

    inlines = [DeadlineChangeInline]

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'name', 'category', 'technical_assignment',
                'author', 'current_responsible', 'version',
                'task', 'acceptance_criteria'
            )
        }),
        ('Сроки (правьте через «Перенести срок»)', {
            'fields': (
                'target_deadline', 'hard_deadline',
                ('time_window_start', 'time_window_end'),
                'conditional_deadline',
                'effective_deadline_readonly',
            )
        }),
        ('Контроль выполнения', {
            'fields': ('control_status', 'control_date', 'result', 'result_description')
        }),
        ('Системная информация', {
            'fields': ('route', 'date_of_creation', 'date_of_change', 'last_editor',
                       'deadline_version','reschedule_count')
        }),
    )

    def effective_deadline_readonly(self, obj):
        return obj.effective_deadline
    effective_deadline_readonly.short_description = "Эффективный срок"

    def overdue_flag(self, obj):
        return "⚠️" if obj.is_overdue() else "—"
    overdue_flag.short_description = "Просрочено?"

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "<int:object_id>/reschedule/",
                self.admin_site.admin_view(self.reschedule_view),
                name="blog_workassignment_reschedule",
            ),
        ]
        return custom + urls

    def reschedule_view(self, request, object_id: int):
        from django.shortcuts import render, redirect, get_object_or_404
        obj = get_object_or_404(WorkAssignment, pk=object_id)

        if request.method == "POST":
            form = RescheduleAdminForm(request.POST)
            if form.is_valid():
                try:
                    WorkAssignmentService.reschedule_deadline(
                        obj,
                        new_target_deadline=form.cleaned_data.get("new_target_deadline"),
                        new_hard_deadline=form.cleaned_data.get("new_hard_deadline"),
                        new_time_window_start=form.cleaned_data.get("new_time_window_start"),
                        new_time_window_end=form.cleaned_data.get("new_time_window_end"),
                        reason=form.cleaned_data.get("reason", ""),
                        user=request.user if request.user.is_authenticated else None,
                        expected_deadline_version=form.cleaned_data["expected_deadline_version"],
                    )
                except ValueError as e:
                    messages.error(request, str(e))
                except RuntimeError as e:
                    messages.error(request, str(e))  # конфликт версий
                else:
                    messages.success(request, "Срок успешно перенесён.")
                    return redirect(f"../change/")
        else:
            form = RescheduleAdminForm(initial={
                "new_target_deadline": obj.target_deadline,
                "new_hard_deadline": obj.hard_deadline,
                "new_time_window_start": obj.time_window_start,
                "new_time_window_end": obj.time_window_end,
                "expected_deadline_version": obj.deadline_version,
            })

        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "original": obj,
            "title": "Перенести срок",
            "form": form,
            "object_id": object_id,
            "has_view_permission": self.has_view_permission(request, obj),
            "has_change_permission": self.has_change_permission(request, obj),
        }
        return render(request, "admin/blog/workassignment/reschedule.html", context)

@admin.register(TechnicalAssignment)
class TechnicalAssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_of_creation', 'last_editor', 'date_of_change', 'current_responsible', 'version')
    search_fields = ('name', 'author__username', 'current_responsible__username')
    list_filter = ('access', 'security', 'post')
    #inlines = [WorkAssignmentInline, RevisionTaskInline, TaskForDesignWorkInline]

    def open_work_assignments_link(self, obj):
        url = reverse('admin:blog_workassignment_changelist') + f'?technical_assignment__id__exact={obj.id}'
        return format_html('<a class="button" href="{}">📂 Открыть РЗ</a>', url)

    open_work_assignments_link.short_description = "Рабочие задания"

    list_display = (
        'id', 'name',
        'work_assignments_count',
        'open_work_assignments_link',
        'add_work_assignment_link',
        'revision_tasks_count',
        'open_revision_tasks_link',
        'add_revision_task_link',
        'design_works_count', 'open_design_works_link', 'add_design_work_link',
    )
    search_fields = ('name',)

    def work_assignments_count(self, obj):
        return obj.work_assignments.count()

    work_assignments_count.short_description = 'РЗ (шт.)'

    def open_work_assignments_link(self, obj):
        # проверь, что app_label = 'blog' и модель = 'workassignment' (обычно так)
        url = reverse('admin:blog_workassignment_changelist') + f'?technical_assignment__id__exact={obj.pk}'
        return format_html('<a class="button" href="{}">📂 Открыть РЗ</a>', url)

    open_work_assignments_link.short_description = 'Рабочие задания'

    def add_work_assignment_link(self, obj):
        url = reverse('admin:blog_workassignment_add') + f'?technical_assignment={obj.pk}'
        return format_html('<a class="button" href="{}">➕ Новое РЗ</a>', url)

    add_work_assignment_link.short_description = 'Создать РЗ'

    class Media:
        css = {'all': ('blog/admin_hscroll.css',)}

    def revision_tasks_count(self, obj):
        return obj.revision_tasks.count()
    revision_tasks_count.short_description = 'Ревизии (шт.)'

    def open_revision_tasks_link(self, obj):
        url = reverse('admin:blog_revisiontask_changelist') + f'?technical_assignment__id__exact={obj.pk}'
        return format_html('<a class="button" href="{}">📂 Открыть ревизии</a>', url)
    open_revision_tasks_link.short_description = 'Список ревизий'

    def add_revision_task_link(self, obj):
        url = reverse('admin:blog_revisiontask_add') + f'?technical_assignment={obj.pk}'
        return format_html('<a class="button" href="{}">➕ Новая ревизия</a>', url)
    add_revision_task_link.short_description = 'Создать ревизию'

    def design_works_count(self, obj):
        return obj.design_works.count()

    design_works_count.short_description = 'ПЗ (шт.)'

    def open_design_works_link(self, obj):
        url = reverse('admin:blog_taskfordesignwork_changelist') + f'?technical_assignment__id__exact={obj.pk}'
        return format_html('<a class="button" href="{}">📂 Открыть ПЗ</a>', url)

    open_design_works_link.short_description = 'Список ПЗ'

    def add_design_work_link(self, obj):
        url = reverse('admin:blog_taskfordesignwork_add') + f'?technical_assignment={obj.pk}'
        return format_html('<a class="button" href="{}">➕ Новое ПЗ</a>', url)

    add_design_work_link.short_description = 'Создать ПЗ'

    # кнопки «Открыть ПЗ» и «Новое ПЗ»
    def design_work_buttons(self, obj):
        list_url = reverse('admin:blog_taskfordesignwork_changelist') + f'?technical_assignment__id__exact={obj.pk}'
        add_url  = reverse('admin:blog_taskfordesignwork_add') + f'?technical_assignment={obj.pk}'
        return format_html(
            '{} {}',
            _btn(list_url, '📂 Открыть ПЗ'),
            _btn(add_url,  '➕ Новое ПЗ'),
        )
    design_work_buttons.short_description = 'Проектные задания'

    class Media:
        css = {'all': ('blog/admin_hscroll.css',)}


try:
    admin.site.unregister(TechnicalAssignment)
except admin.sites.NotRegistered:
    pass
admin.site.register(TechnicalAssignment, TechnicalAssignmentAdmin)

autocomplete_fields = ['post']  # удобно выбирать пост вручную при необходимости


def get_changeform_initial_data(self, request):
    initial = super().get_changeform_initial_data(request)
    post_id = request.GET.get('post')
    if post_id:
        initial['post'] = post_id
    return initial

@admin.register(WorkAssignmentDeadlineChange)
class WorkAssignmentDeadlineChangeAdmin(admin.ModelAdmin):
    list_display = ("id","assignment","changed_by","changed_at",
                    "old_target_deadline","new_target_deadline",
                    "old_hard_deadline","new_hard_deadline")
    list_filter = ("changed_by","changed_at")
    search_fields = ("assignment__name","reason")

