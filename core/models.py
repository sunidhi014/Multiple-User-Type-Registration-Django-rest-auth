from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_employer = models.BooleanField(default=False)
  is_emp = models.BooleanField(default=False)

class Emp(models.Model):
    emp = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    Emp_code = models.CharField(max_length=100)
    department = models.TextField()

    def __str__(self):
        return self.emp.username

class Employer(models.Model):
    employer = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.employer.username
