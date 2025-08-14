from django import forms

class RescheduleAdminForm(forms.Form):
    new_target_deadline = forms.DateField(required=False, label="Новый целевой срок")
    new_hard_deadline = forms.DateField(required=False, label="Новый абсолютный срок")
    new_time_window_start = forms.DateField(required=False, label="Окно: с")
    new_time_window_end = forms.DateField(required=False, label="Окно: по")
    reason = forms.CharField(required=False, label="Причина", widget=forms.TextInput(attrs={"size": 80}))
    expected_deadline_version = forms.IntegerField(widget=forms.HiddenInput)
