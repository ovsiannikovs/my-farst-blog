from django.db import models
from django.contrib.auth.models import User


# 🔧 Заглушки / вспомогательные модели
class TechnicalAssignment(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class DesignDocumentation(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class WorkingDocumentation(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class PilotSample(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Procurement(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class ProductionLaunch(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Production(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Sales(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Patenting(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class ConformityAssessment(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title


# ✅ Модель Post
class Post(models.Model):
    name = models.CharField(max_length=100)
    design_product = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='edited_posts')
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_posts')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_change = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=20)
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=20)
    trl = models.CharField(max_length=10)

    # Связи
    technical_assignments = models.ManyToManyField(TechnicalAssignment, blank=True)
    design_documentation = models.OneToOneField(DesignDocumentation, on_delete=models.SET_NULL, null=True, blank=True)
    working_documentation = models.OneToOneField(WorkingDocumentation, on_delete=models.SET_NULL, null=True, blank=True)
    pilot_samples = models.OneToOneField(PilotSample, on_delete=models.SET_NULL, null=True, blank=True)
    procurement = models.ManyToManyField(Procurement, blank=True)
    production_launch = models.OneToOneField(ProductionLaunch, on_delete=models.SET_NULL, null=True, blank=True)
    production = models.OneToOneField(Production, on_delete=models.SET_NULL, null=True, blank=True)
    sales = models.OneToOneField(Sales, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True, blank=True)
    patenting = models.ManyToManyField(Patenting, blank=True)
    conformity_assessment = models.OneToOneField(ConformityAssessment, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Разработка"
        verbose_name_plural = "Разработки"

    def __str__(self):
        return self.name


# ✅ Вспомогательные сущности для TechnicalProposal
class GeneralDrawingProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ElectronicModelProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class GeneralElectricalCircuit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ProductSoftware(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ReportTechnicalProposal(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ProtocolTechnicalProposal(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class DrawingUnit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ElectronicModelUnit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class DrawingPartUnit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ElectronicModelPartUnit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class DrawingPartProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ElectronicModelPartProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class AddReportTechnicalProposal(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class ListTechnicalProposal(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name


# ✅ Основная модель TechnicalProposal
class TechnicalProposal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, related_name='tp_created_by', on_delete=models.SET_NULL, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_editor = models.ForeignKey(User, related_name='tp_last_edited_by', on_delete=models.SET_NULL, null=True)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, related_name='tp_current_responsible', on_delete=models.SET_NULL, null=True)
    version = models.CharField(max_length=20, blank=True)
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')

    list_technical_proposal = models.OneToOneField(ListTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)
    general_drawing_product = models.OneToOneField(GeneralDrawingProduct, on_delete=models.SET_NULL, null=True, blank=True)
    electronic_model_product = models.OneToOneField(ElectronicModelProduct, on_delete=models.SET_NULL, null=True, blank=True)
    general_electrical_circuit = models.OneToOneField(GeneralElectricalCircuit, on_delete=models.SET_NULL, null=True, blank=True)
    product_software = models.OneToOneField(ProductSoftware, on_delete=models.SET_NULL, null=True, blank=True)
    report_technical_proposal = models.OneToOneField(ReportTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)
    protocol_technical_proposal = models.OneToOneField(ProtocolTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)

    general_drawing_unit = models.ManyToManyField(DrawingUnit, blank=True)
    electronic_model_unit = models.ManyToManyField(ElectronicModelUnit, blank=True)
    drawing_part_unit = models.ManyToManyField(DrawingPartUnit, blank=True)
    electronic_model_part_unit = models.ManyToManyField(ElectronicModelPartUnit, blank=True)
    drawing_part_product = models.ManyToManyField(DrawingPartProduct, blank=True)
    electronic_model_part_product = models.ManyToManyField(ElectronicModelPartProduct, blank=True)
    add_report_technical_proposal = models.ManyToManyField(AddReportTechnicalProposal, blank=True)

    class Meta:
        verbose_name = "Техническое предложение"
        verbose_name_plural = "Технические предложения"

    def __str__(self):
        return self.name
