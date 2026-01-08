from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['full_name', 'email', 'text']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Ваше ФИО'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш email'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Напишите ваш отзыв...',
                'rows': 4
            }),
        }
