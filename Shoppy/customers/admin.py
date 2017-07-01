from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'address',)
	search_fields = ('name', 'email',)