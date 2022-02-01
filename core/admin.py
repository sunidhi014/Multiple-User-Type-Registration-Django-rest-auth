from django.contrib import admin
from core.models import Emp, Employer, User
admin.site.register(User)
admin.site.register(Emp)
admin.site.register(Employer)