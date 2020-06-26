from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'state', 'city', 'pincode',
     'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'realtor')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 
    'pincode', 'price')

admin.site.register(Listing, ListingAdmin)
