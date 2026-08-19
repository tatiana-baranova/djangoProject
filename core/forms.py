from django import forms 
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        label='Тема листа',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Тема листа'
            }
        )
    )

    email = forms.EmailField(
        label='Ваша електронна адреса',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ваша електронна адреса'
            }
        )
    )

    message = forms.CharField(
        label='Текст повідомлення',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введіть текст повідомлення',
                'rows': 5
            }
        )
    )

    class Meta:
        model = ContactMessage
        fields = ['subject', 'email', 'message']