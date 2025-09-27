from django.contrib import admin
from django.contrib.auth.models import User
from .models import PetType, Veterinarian, Appointment

# Register User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']

# Register Veterinarian model
@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'contact']
    list_filter = ['specialization']

# Register PetType model
@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

# Register Appointment model
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['pet_type', 'vet', 'appointment_date', 'appointment_time', 'status']
    list_filter = ['status', 'appointment_date', 'vet']
    search_fields = ['pet_type__name', 'owner__username']