from django import forms
from django.utils import timezone
from .models import WorkAssignment

class WorkAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkAssignment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.deadline and timezone.now().date() >= instance.deadline:
            self.fields['result'].required = True
