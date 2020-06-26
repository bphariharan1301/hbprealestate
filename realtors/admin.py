from django.contrib import admin
from .models import Realtor

# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'phone', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'hire_date')
    list_editable = ('is_mvp',)
    search_fields = ('id', 'name')

admin.site.register(Realtor, RealtorAdmin)