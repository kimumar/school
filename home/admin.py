from django.contrib import admin
from . models import ContactMessage
# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('name', 'created')
    search_fields = ('name', 'email', 'message')




admin.site.register(ContactMessage, ContactMessageAdmin)