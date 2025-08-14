from django import forms
from django.utils import timezone
from .models import WorkAssignment


class WorkAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkAssignment
        fields = "__all__"
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'target_deadline': forms.DateInput(attrs={'type': 'date'}),
            'hard_deadline': forms.DateInput(attrs={'type': 'date'}),
            'time_window_start': forms.DateInput(attrs={'type': 'date'}),
            'time_window_end': forms.DateInput(attrs={'type': 'date'}),
            'control_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = timezone.localdate()
        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            if instance.deadline and today >= instance.deadline:
                self.fields['result'].required = True

            if instance.target_deadline and today >= instance.target_deadline:
                self.fields['control_date'].required = True

    def clean(self):
        cleaned = super().clean()
        today = timezone.localdate()

        deadline = cleaned.get('deadline')
        target_deadline = cleaned.get('target_deadline')
        result = cleaned.get('result')
        control_date = cleaned.get('control_date')
        tw_start = cleaned.get('time_window_start')
        tw_end = cleaned.get('time_window_end')

        # валидация окна
        if tw_start and tw_end and tw_end < tw_start:
            self.add_error('time_window_end', 'Дата «по» не может быть раньше даты «с».')

        if deadline and today >= deadline and not result:
            self.add_error('result', 'После наступления срока выполнения нужно выбрать результат.')

        if target_deadline and today >= target_deadline and not control_date:
            self.add_error('control_date', 'После наступления целевого срока необходимо указать дату контроля.')

        return cleaned