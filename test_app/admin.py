from django.contrib import admin
from .models import Department, Test, User, Order, Result, Report_Admin, Login_Manager
# Register your models here.
admin.site.register(Department)
admin.site.register(Test)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Result)
admin.site.register(Report_Admin)
admin.site.register(Login_Manager)