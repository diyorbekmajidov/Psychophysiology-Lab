from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('To\'liq ismingiz'),
                'class': 'form-control',
                'id': 'contact-name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _('email@manzil.uz'),
                'class': 'form-control',
                'id': 'contact-email',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': _('Mavzu'),
                'class': 'form-control',
                'id': 'contact-subject',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': _('Xabaringiz...'),
                'class': 'form-control',
                'rows': 6,
                'id': 'contact-message',
            }),
        }
        labels = {
            'name':    _("To'liq ism"),
            'email':   _('Email manzil'),
            'subject': _('Mavzu'),
            'message': _('Xabar'),
        }
