from django import forms
from .models import Appointment, PetType

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["pet_type", "vet", "appointment_date", "appointment_time", "reason"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields["pet_type"].queryset = PetType.objects.all()