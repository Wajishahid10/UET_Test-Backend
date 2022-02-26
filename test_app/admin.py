from django.contrib import admin
from .models import Department, Test, User, Order, Result, Login_Manager, Admin, PersonAssignedforOrder, Test_Images
# Register your models here.
admin.site.register(Department)
admin.site.register(Test)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Result)
admin.site.register(Login_Manager)
admin.site.register(Admin)
admin.site.register(PersonAssignedforOrder)
admin.site.register(Test_Images)