#!/usr/bin/env python
"""
Run this script once after migrations to create the default admin user.
Usage: python seed_admin.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        password='admin123',
        email='admin@hospital.com',
        first_name='Admin'
    )
    print("✅ Default admin user created: username=admin, password=admin123")
else:
    print("ℹ️  Admin user already exists.")
