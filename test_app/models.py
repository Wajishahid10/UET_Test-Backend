from distutils import extension
from email.message import EmailMessage
from xml.parsers.expat import model
from django.db import models

import uuid


def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid3().hex
        return f'images/{uuidHex}.{extension}'

# Models here.

class Login_Manager(models.Model):
    Email_Address=models.CharField(max_length= 100)
    Passwords=models.CharField(max_length= 100)

class User(models.Model):
    User_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Company=models.CharField(max_length= 100)
    Contact_Number= models.IntegerField()
    Email_Address=models.ForeignKey(Login_Manager, on_delete=models.CASCADE)

class Admin(models.Model):
    Admin_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Role=models.IntegerField()
    Contact_Number= models.IntegerField()
    Email_Address=models.ForeignKey(Login_Manager, on_delete=models.CASCADE)

AdminRoles_Dict={1:'Admin',2:'Chariman',3:'Instructor',4:'Lab Opertaor'}

class Department(models.Model):
    Department_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Display_picture=models.ImageField(upload_to=convert_Image_Name)
    Admin_ID=models.ForeignKey(Admin, on_delete=models.CASCADE)
    Contact_Number= models.IntegerField()
    Email_Address=models.CharField(max_length= 100)
    
class Test(models.Model):
    Test_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Department_ID=models.ForeignKey(Department, on_delete=models.CASCADE)
    Description=models.TextField(max_length= 1000)
    Estimates_Testing_Time=models.TimeField()
    Test_Sample_Attributes=models.JSONField()
    Test_Sample_Respectivley=models.JSONField()
    Price=models.IntegerField()
    Test_Times=models.IntegerField()

class Test_Images(models.Model):
    Test_Images_ID=models.ForeignKey(Test, on_delete=models.CASCADE, primary_key=True)
    Image=models.ImageField(upload_to=convert_Image_Name)

class Order(models.Model):
    Order_ID=models.AutoField(primary_key=True)
    User_ID=models.ForeignKey(User, on_delete=models.CASCADE)
    Test_ID=models.ForeignKey(Test, on_delete=models.CASCADE)
    OrderCompletionTime=models.DateTimeField()
    Status=models.TextField(max_length=15)
    Total_Bill=models.IntegerField()


PersonAssigned_Dict={1:'Supervision',2:'Research',3:'Assisst',4:'Operate'}

# People Assigned for each after confirmation of Chairman of Department
class PersonAssignedforOrder(models.Model):
    GroupPerson_ID=models.AutoField(primary_key=True)
    Order_ID=models.ForeignKey(Order, on_delete=models.CASCADE)
    Admin_ID=models.ForeignKey(Admin, on_delete=models.CASCADE)
    #AssignedResponsibility=models.CharField(max_length= 45)

class CompletedOrder(models.Model):
    Order_ID=models.IntegerField(primary_key=True)
    User_ID=models.ForeignKey(User, on_delete=models.CASCADE)
    Test_ID=models.ForeignKey(Test, on_delete=models.CASCADE)
    DeliveryTime=models.DateTimeField()
    Status=models.TextField(max_length=15)
    Total_Bill=models.IntegerField()

class Result(models.Model):
    Result_ID=models.AutoField(primary_key=True)
    Order_ID=models.ForeignKey(Order, on_delete=models.CASCADE)
    Result=models.CharField(max_length=50)
    Image=models.ImageField(upload_to=convert_Image_Name)
    Details=models.JSONField()

class Report_Admin(models.Model):
    Report_Admin_ID=models.AutoField(primary_key=True)
    Department_ID=models.ForeignKey(Department, on_delete=models.CASCADE)
    Name=models.CharField(max_length= 100)
    Contact_Number= models.IntegerField()
    Email_Address=models.CharField(max_length= 100)
