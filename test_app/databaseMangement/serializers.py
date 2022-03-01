from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models import Department, Test, User, Order, Result, Login_Manager, Admin, Test_Images, PersonAssignedforOrder, CompletedOrder


class Login_ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login_Manager
        fields= '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields= '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields= '__all__'

class Test_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test_Images
        fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields= '__all__'

class PersonAssignedforOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonAssignedforOrder
        fields= '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields= '__all__'

class CompletedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompletedOrder
        fields= '__all__'