from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "appointments"

urlpatterns = [
    path("", views.index, name="appointments_index"),
    path("book/", views.book_appointment, name="book_appointment"),
    path("my/", views.my_appointments, name="my_appointments"),
    path("admin-appointments/", views.admin_appointments, name="admin_appointments"),
    path("approve/<int:appointment_id>/", views.approve_appointment, name="approve_appointment"),
    path("deny/<int:appointment_id>/", views.deny_appointment, name="deny_appointment"),

   # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="appointments/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),


]


