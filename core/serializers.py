from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from core.models import Emp, Employer

class EmpCustomRegistrationSerializer(RegisterSerializer):
    emp = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    Emp_code = serializers.CharField(required=True)
    department = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(EmpCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'Emp_code' : self.validated_data.get('Emp_code', ''),
                'department': self.validated_data.get('department', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(EmpCustomRegistrationSerializer, self).save(request)
        user.is_emp = True
        user.save()
        emp = Emp(emp =user, Emp_code=self.cleaned_data.get('Emp_code'), 
                department=self.cleaned_data.get('department'))
        emp.save()
        return user


class EmployerCustomRegistrationSerializer(RegisterSerializer):
    employer = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    country = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(EmployerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'country' : self.validated_data.get('country', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(EmployerCustomRegistrationSerializer, self).save(request)
        user.is_employer = True
        user.save()
        employer = Employer(employer=user,country=self.cleaned_data.get('country'))
        employer.save()
        return user