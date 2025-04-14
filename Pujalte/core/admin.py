from django.contrib import admin
from .models import ContactForm

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nombre','correo','teléfono',)

# Register your models here.
admin.site.register(ContactForm)