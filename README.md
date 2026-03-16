# 🏥 Hospital Management System — Django

A full-featured Hospital Management System converted from Flask + MySQL to **Django + SQLite**.

## Features
- 🔐 User Authentication (Login, Register, Logout)
- 📊 Dashboard with live stats (patients, doctors, appointments)
- 👥 Patient Management (Add, Edit, Delete, Search)
- 🩺 Doctor Management (Add, Delete)
- 📅 Appointment Booking & Status Management
- 🎨 Same original UI/CSS — pixel-perfect conversion

---

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
        └── style.css              # Original CSS (unchanged)
```

---

## Flask → Django Changes

| Flask | Django Equivalent |
|-------|------------------|
| `mysql-connector` | Django ORM + SQLite |
| `session['user_id']` | `request.user` (Django auth) |
| `flash(msg, 'success')` | `messages.success(request, msg)` |
| `url_for('view_name')` | `{% url 'name' %}` |
| `@login_required` decorator | `@login_required` decorator |
| Raw SQL queries | Django QuerySet ORM |
| `db.py` | `models.py` + migrations |
| `app.py` | `views.py` + `urls.py` |
| SHA-256 password hashing | Django's built-in PBKDF2 hashing |
