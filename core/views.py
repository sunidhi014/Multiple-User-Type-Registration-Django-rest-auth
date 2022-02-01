from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    EmpCustomRegistrationSerializer, EmployerCustomRegistrationSerializer
    )

class EmpRegistrationView(RegisterView):
    serializer_class = EmpCustomRegistrationSerializer


class EmployerRegistrationView(RegisterView):
    serializer_class = EmployerCustomRegistrationSerializer
