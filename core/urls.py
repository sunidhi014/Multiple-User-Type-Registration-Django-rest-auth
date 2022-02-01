from django.urls import include, path
from django.conf.urls import url

from core.views import EmpRegistrationView, EmployerRegistrationView
app_name = 'core'
urlpatterns = [
     #Registration Urls
    path('registration/emp/', EmpRegistrationView.as_view(), name='register-emp'),
    path('registration/employer/', EmployerRegistrationView.as_view(), name='register-employer'),
]