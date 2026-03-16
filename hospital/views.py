from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count

from .models import Patient, Doctor, Appointment
from .forms import LoginForm, RegisterForm, PatientForm, DoctorForm, AppointmentForm


# ── AUTH ──────────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm(request)

    return render(request, 'hospital/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['full_name']
            role = form.cleaned_data['role']
            user.save()
            # Store role in profile via is_staff / is_superuser or just session
            # We'll use the profile approach via a simple attribute on request
            request.session['user_role'] = role
            messages.success(request, f"Account created successfully! Welcome, {user.username}. Please log in.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegisterForm()

    return render(request, 'hospital/register.html', {'form': form})


# ── DASHBOARD ─────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    today = timezone.now().date()
    stats = {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appointments': Appointment.objects.count(),
        'today': Appointment.objects.filter(date=today).count(),
    }
    recent = Appointment.objects.select_related('patient', 'doctor').order_by('-id')[:5]
    return render(request, 'hospital/dashboard.html', {'stats': stats, 'recent': recent})


# ── PATIENTS ──────────────────────────────────────────────────────────────────

@login_required
def patients(request):
    search = request.GET.get('search', '').strip()
    qs = Patient.objects.all()
    if search:
        qs = qs.filter(Q(name__icontains=search) | Q(disease__icontains=search))
    return render(request, 'hospital/patients.html', {'patients': qs, 'search': search})


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})


@login_required
def edit_patient(request, pid):
    patient = get_object_or_404(Patient, pk=pid)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital/edit_patient.html', {'form': form, 'patient': patient})


@login_required
def delete_patient(request, pid):
    patient = get_object_or_404(Patient, pk=pid)
    patient.delete()
    messages.info(request, 'Patient deleted.')
    return redirect('patients')


# ── DOCTORS ───────────────────────────────────────────────────────────────────

@login_required
def doctors(request):
    qs = Doctor.objects.all()
    return render(request, 'hospital/doctors.html', {'doctors': qs})


@login_required
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully!')
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'hospital/add_doctor.html', {'form': form})


@login_required
def delete_doctor(request, did):
    doctor = get_object_or_404(Doctor, pk=did)
    doctor.delete()
    messages.info(request, 'Doctor removed.')
    return redirect('doctors')


# ── APPOINTMENTS ──────────────────────────────────────────────────────────────

@login_required
def appointments(request):
    qs = Appointment.objects.select_related('patient', 'doctor').order_by('-date', '-id')
    return render(request, 'hospital/appointments.html', {'appointments': qs})


@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/add_appointment.html', {'form': form})


@login_required
def delete_appointment(request, aid):
    appointment = get_object_or_404(Appointment, pk=aid)
    appointment.delete()
    messages.info(request, 'Appointment deleted.')
    return redirect('appointments')


@login_required
def update_appointment_status(request, aid, status):
    allowed = ['Scheduled', 'Completed', 'Cancelled']
    if status not in allowed:
        messages.error(request, 'Invalid status.')
        return redirect('appointments')
    appointment = get_object_or_404(Appointment, pk=aid)
    appointment.status = status
    appointment.save()
    messages.success(request, f'Appointment marked as {status}.')
    return redirect('appointments')
