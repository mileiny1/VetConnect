
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.http import HttpResponse

from .models import Appointment
from .forms import AppointmentForm
from django.urls import reverse

from .models import Appointment, Veterinarian


# --------------------------
# 🔐 Custom User Setup
# --------------------------

User = get_user_model()  # Always use this when AUTH_USER_MODEL is swapped


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")  # add extra fields if your User has them


# --------------------------
# 🌐 Views
# --------------------------

def index(request):
    return render(request, "appointments/appointments_index.html")


def register(request):
    """ Custom user registration """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            messages.success(request, "Account created successfully!")
            return redirect("/appointments/my/")
    else:
        form = CustomUserCreationForm()
    return render(request, "appointments/register.html", {"form": form})

##
def custom_login(request):
    """ Custom login view (instead of Django default) """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("appointments:my_appointment")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "appointments/login.html", {"form": form})

@login_required
def logout_view(request):
    """Log out the current user"""
    logout(request)
    messages.info(request, "You have been logged out successfully!")
    return redirect("/appointments/logout/")  # Redirect to login page after logout


# --------------------------
# 👤 USER VIEWS
# --------------------------
@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)  # ✅ removed `user=request.user`
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user  # still attach the logged-in user
            try:
                appointment.clean()
                appointment.save()
                messages.success(request, "Appointment booked successfully! Pending admin approval.")
                return redirect("/appointments/my/")
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = AppointmentForm()  # ✅ removed `user=request.user`
    return render(request, "appointments/book_appointment.html", {"form": form})

@login_required
def my_appointments(request):
    """Show only the appointments of the logged-in user."""
    appointments = Appointment.objects.filter(owner=request.user).order_by("-appointment_date", "-appointment_time")
    return render(request, "appointments/my_appointments.html", {"appointments": appointments})


# --------------------------
# 🛠️ ADMIN VIEWS
# --------------------------

@user_passes_test(lambda u: u.is_staff)
def admin_appointments(request):
    """Allow admins/staff to view and manage all appointments."""
    appointments = Appointment.objects.all().order_by("-appointment_date", "-appointment_time")
    return render(request, "appointments/admin_appointments.html", {"appointments": appointments})


@user_passes_test(lambda u: u.is_staff)
def approve_appointment(request, appointment_id):
    """Admin can approve an appointment."""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "approved"
    appointment.save()
    messages.success(request, "✅ Appointment approved!")
    return redirect("admin_appointments")


@user_passes_test(lambda u: u.is_staff)
def deny_appointment(request, appointment_id):
    """Admin can deny an appointment."""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "denied"
    appointment.save()
    messages.error(request, "❌ Appointment denied.")
    return redirect("admin_appointments")
