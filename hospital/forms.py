from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'autofocus': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'id': 'password'})
    )


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [('staff', 'Staff'), ('doctor', 'Doctor'), ('admin', 'Admin')]

    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Your full name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'})
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimum 6 characters', 'id': 'password', 'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password', 'id': 'confirm_password', 'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'role', 'password1', 'password2']

    def clean_password1(self):
        pw = self.cleaned_data.get('password1')
        if pw and len(pw) < 6:
            raise forms.ValidationError('Password must be at least 6 characters.')
        return pw


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'disease', 'phone', 'blood_group']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'min': 0, 'max': 150}),
            'disease': forms.TextInput(attrs={'placeholder': 'e.g. Diabetes, Hypertension'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Contact number'}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'phone', 'email', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Dr. Sharma'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Contact number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'doctor@hospital.com'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'e.g. 10', 'min': 0}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Any additional notes...', 'rows': 3}),
        }
