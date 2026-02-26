from django.contrib import admin
from .models import Appointment, Doctor

@admin.action(description="Approve selected appointments")
def approve_appointments(modeladmin, request, queryset):
    queryset.update(status="APPROVED")

@admin.action(description="Reject selected appointments")
def reject_appointments(modeladmin, request, queryset):
    queryset.update(status="REJECTED")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "date", "time", "status")
    list_filter = ("status", "doctor", "date")
    search_fields = ("patient__username", "doctor__name")
    actions = [approve_appointments, reject_appointments]

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")