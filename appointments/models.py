from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser # its going to be create automatically the users information.
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# -------------------
# Custom User Model
# -------------------
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.username

# -------------------
# Veterinarian Model
# -------------------
class Veterinarian(models.Model):
    VET_CHOICES = [
        ('dr_sarah_smith', 'Dr. Sarah Smith - Small Animal Specialist'),
        ('dr_michael_jones', 'Dr. Michael Jones - Exotic Animal Specialist'),
        ('dr_emily_davis', 'Dr. Emily Davis - Large Animal Specialist'),
        ('dr_robert_wilson', 'Dr. Robert Wilson - Surgery Specialist'),
        ('dr_lisa_brown', 'Dr. Lisa Brown - Emergency Care Specialist'),
        ('dr_james_taylor', 'Dr. James Taylor - Internal Medicine'),
        ('dr_amanda_white', 'Dr. Amanda White - Dermatology Specialist'),
        ('dr_david_miller', 'Dr. David Miller - Orthopedic Specialist'),
    ]
   
    SPECIALIZATION_CHOICES = [
        ('small_animals', 'Small Animals'),
        ('large_animals', 'Large Animals'),
        ('exotic_animals', 'Exotic Animals'),
        ('surgery', 'Surgery'),
        ('emergency_care', 'Emergency Care'),
        ('internal_medicine', 'Internal Medicine'),
        ('dermatology', 'Dermatology'),
        ('orthopedics', 'Orthopedics'),
        ('cardiology', 'Cardiology'),
        ('oncology', 'Oncology'),
    ]
   
    name = models.CharField(max_length=150, choices=VET_CHOICES)
    specialization = models.CharField(max_length=150, choices=SPECIALIZATION_CHOICES)
    contact = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.get_name_display()
#------------------
# Pet Type Model
#------------------
class PetType(models.Model):
    name = models.CharField(max_length=100, unique=True) # e.g. Dog, Cat, Rabbit

    def __str__(self):
        return self.name


# -------------------
# Appointment Model
# -------------------
class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("denied", "Denied"),
    ]
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    vet = models.ForeignKey(Veterinarian, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
   
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["vet", "appointment_date", "appointment_time"],
                name="unique_vet_appointment"
            )
        ]
   
    def clean(self):
        """ Prevent double booking of the same vet at the same date and time """
        if self.vet:
            conflict = Appointment.objects.filter(
                vet=self.vet,
                appointment_date=self.appointment_date,
                appointment_time=self.appointment_time,
            ).exclude(id=self.id)
            if conflict.exists():
                raise ValidationError("This time slot is already booked with this vet.")
   
    def save(self, *args, **kwargs):
        self.full_clean()  # ensures `clean()` is called
        super().save(*args, **kwargs)
   
    def __str__(self):
        vet_name = self.vet.get_name_display() if self.vet else "No vet"
        return f"{self.pet_type} with {vet_name} on {self.appointment_date} at {self.appointment_time}"
