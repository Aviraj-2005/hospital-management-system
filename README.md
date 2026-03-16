
# 🏥 Hospital Management System — Django

A full-featured Hospital Management System  **Django + SQLite**.

## Features
- 🔐 User Authentication (Login, Register, Logout)
- 📊 Dashboard with live stats (patients, doctors, appointments)
- 👥 Patient Management (Add, Edit, Delete, Search)
- 🩺 Doctor Management (Add, Delete)
- 📅 Appointment Booking & Status Management
- 🎨 Same original UI/CSS — pixel-perfect conversion

---
## Live : https://hospital-management-system-ax6c.onrender.com

## Setup & Run

### 1. Install Django
```bash
pip install -r requirements.txt
```

### 2. Apply database migrations
```bash
python manage.py migrate
```

### 3. Create the default admin user
```bash
python seed_admin.py
```

### 4. Run the development server
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://127.0.0.1:8000/
```

**Default login:** `admin` / `admin123`

---

## Project Structure

```
hospital_django/
├── manage.py
├── requirements.txt
├── seed_admin.py                  # Creates default admin user
├── hospital.db                    # SQLite database (auto-created)
├── hospital_management/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── hospital/                      # Main app
    ├── models.py                  # Patient, Doctor, Appointment
    ├── views.py                   # All view logic
    ├── forms.py                   # Django ModelForms
    ├── urls.py                    # URL routing
    ├── admin.py                   # Django admin registration
    ├── migrations/
    │   └── 0001_initial.py
    ├── templates/hospital/        # All HTML templates
    │   ├── base.html
    │   ├── login.html
    │   ├── register.html
    │   ├── dashboard.html
    │   ├── patients.html
    │   ├── add_patient.html
    │   ├── edit_patient.html
    │   ├── doctors.html
    │   ├── add_doctor.html
    │   ├── appointments.html
    │   └── add_appointment.html
    └── static/hospital/
        └── style.css              # Original CSS





