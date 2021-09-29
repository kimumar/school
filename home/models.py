from django.db import models
from django.forms import  TextInput, EmailInput, FileInput, Select, Textarea
from django.forms import ModelForm
# Create your models here.
class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    subject = models.CharField(null=True, blank=True, max_length=200)
    message = models.CharField(null=True, blank=True, max_length=2000)
    status = models.CharField(blank=True, null=True, max_length=200, choices=STATUS, default='New')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets= {
            'name' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'subject' : TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'email' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message' : Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '5'}),
        }
