from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Patients
    path('patients/', views.patients, name='patients'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/edit/<int:pid>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:pid>/', views.delete_patient, name='delete_patient'),

    # Doctors
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/delete/<int:did>/', views.delete_doctor, name='delete_doctor'),

    # Appointments
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/delete/<int:aid>/', views.delete_appointment, name='delete_appointment'),
    path('appointments/status/<int:aid>/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
]
