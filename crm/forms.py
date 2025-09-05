from django import forms
from .models import TicketComment, KnowledgeBaseArticle, SupportTicket

class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['text', 'file']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Введите комментарий...',
                'class': 'vLargeTextField'
            }),
        }

class KnowledgeBaseArticleForm(forms.ModelForm):
    class Meta:
        model = KnowledgeBaseArticle
        fields = ['title', 'category', 'content', 'status', 'file']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 15,
                'class': 'vLargeTextField'
            }),
            'title': forms.TextInput(attrs={'size': 60}),
        }

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['customer', 'product', 'category', 'problem', 'description', 'status', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 8, 'class': 'vLargeTextField'}),
            'problem': forms.TextInput(attrs={'size': 60}),
        }