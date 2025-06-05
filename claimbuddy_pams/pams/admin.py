
# Register your models here.
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age', 'gender', 'insurance_provider', 'policy_number', 'created_at']
    list_filter = ['gender', 'insurance_provider', 'created_at']
    search_fields = ['full_name', 'policy_number', 'insurance_provider']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'age', 'gender')
        }),
        ('Insurance Information', {
            'fields': ('insurance_provider', 'policy_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )