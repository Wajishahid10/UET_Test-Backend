from distutils import extension
from email.message import EmailMessage
from xml.parsers.expat import model
from django.db import models

import uuid


# Models here.

class Login_Manager(models.Model):
    GoogleSiginUID=models.CharField(max_length= 50)
    Account_Type=models.CharField(max_length= 7)

class User(models.Model):
    def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid4().hex
        return f'images/{uuidHex}.{extension}'


    User_ID=models.OneToOneField(
        Login_Manager,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Name=models.CharField(max_length= 100)
    Display_picture=models.ImageField(upload_to=convert_Image_Name)
    Company=models.CharField(max_length= 100)
    Contact_Number= models.CharField(max_length= 15)
    Address=models.CharField(max_length= 375)
    Email_Address=models.CharField(max_length= 75)
    AccountCreated = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid4().hex
        return f'images/{uuidHex}.{extension}'


    Admin_ID=models.OneToOneField(
        Login_Manager,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Name=models.CharField(max_length= 100)
    Display_picture=models.ImageField(upload_to=convert_Image_Name)
    Role= models.CharField(max_length= 15)
    Contact_Number= models.CharField(max_length= 15)
    Address=models.CharField(max_length= 375)
    Email_Address=models.CharField(max_length= 75)
    AccountCreated = models.DateTimeField(auto_now_add=True)

AdminRoles_Dict={1:'Admin',2:'Chariman',3:'Instructor',4:'Lab Opertaor'}

class Department(models.Model):
    def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid4().hex
        return f'images/{uuidHex}.{extension}'

    Department_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Display_picture=models.ImageField(upload_to=convert_Image_Name)
    Admin_ID=models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    Contact_Number_toDisplay= models.CharField(max_length= 15)
    Email_Address=models.CharField(max_length= 100)
    DepartmentCreated = models.DateTimeField(auto_now_add=True)
    
class Test(models.Model):
    Test_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100)
    Department_ID=models.ForeignKey(Department, on_delete=models.CASCADE)
    Description=models.TextField(max_length= 1000)
    Estimates_Testing_Time=models.CharField(max_length= 30)
    Test_Sample_Attributes=models.JSONField()
    # Test_Sample_Respectivley=models.JSONField()
    Price=models.IntegerField()
    Test_Counts=models.IntegerField()
    TestCreated = models.DateTimeField(auto_now_add=True)

class Test_Images(models.Model):
    def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid4().hex
        return f'images/{uuidHex}.{extension}'

    Test_Images_ID=models.ForeignKey(Test, on_delete=models.CASCADE)
    Image=models.ImageField(upload_to=convert_Image_Name)

class Order(models.Model):
    Order_ID=models.AutoField(primary_key=True)
    User_ID=models.ForeignKey(User, on_delete=models.CASCADE)
    Test_ID=models.ForeignKey(Test, on_delete=models.CASCADE)
    Test_Sample_Attributes=models.JSONField()
    OrderCompletionTime=models.CharField(max_length= 30)
    Status=models.TextField(max_length=15)
    Total_Bill=models.IntegerField()


#   PersonAssigned_Dict={1:'Supervision',2:'Research',3:'Assisst',4:'Operate'}

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
    DeliveryTime=models.CharField(max_length= 30)
    Status=models.TextField(max_length=15)
    Total_Bill=models.IntegerField()

class Result(models.Model):
    def convert_Image_Name(Instance,Image_Name):
        extension=Image_Name.split('.')[-1]
        uuidHex=uuid.uuid4().hex
        return f'images/{uuidHex}.{extension}'
        
    Result_ID=models.AutoField(primary_key=True)
    Order_ID=models.ForeignKey(Order, on_delete=models.CASCADE)
    Result=models.CharField(max_length=50)
    Image=models.ImageField(upload_to=convert_Image_Name)
    Details=models.JSONField()


