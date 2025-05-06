from django.db import models
from django.contrib.auth.models import User


# Заглушки для связанных сущностей:
class TechnicalAssignment(models.Model):
    title = models.CharField(max_length=255)

class DesignDocumentation(models.Model):
    title = models.CharField(max_length=255)

class WorkingDocumentation(models.Model):
    title = models.CharField(max_length=255)

class PilotSample(models.Model):
    title = models.CharField(max_length=255)

class Procurement(models.Model):
    title = models.CharField(max_length=255)

class ProductionLaunch(models.Model):
    title = models.CharField(max_length=255)

class Production(models.Model):
    title = models.CharField(max_length=255)

class Sales(models.Model):
    title = models.CharField(max_length=255)

class Service(models.Model):
    title = models.CharField(max_length=255)

class Patenting(models.Model):
    title = models.CharField(max_length=255)

class ConformityAssessment(models.Model):
    title = models.CharField(max_length=255)


class Post(models.Model):
    name = models.CharField(max_length=100)
    desig_product = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='edited_posts')
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_posts')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_change = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=20)
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=20)
    trl = models.CharField(max_length=10)

    # Связи из ТЗ:
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

    def __str__(self):
        return self.name
