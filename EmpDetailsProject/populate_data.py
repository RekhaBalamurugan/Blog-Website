import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','EmpDetailsProject.settings')

import django
django.setup()

import random
from EmployeeApp.models import Users
from faker import Faker
from django.shortcuts import redirect,render

fake=Faker()

def populate(N):

    for entry in range(N):
        fake_firstname=fake.first_name()
        fake_lastname=fake.last_name()
        fake_email=fake.email()

        userinfo= Users.objects.get_or_create(firstname=fake_firstname,lastname=fake_lastname,email=fake_email)[0]

if __name__=='__main__':
    populate(10)





