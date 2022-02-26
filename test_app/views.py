from cmath import exp
from importlib.resources import contents
from django.shortcuts import render
from .models import Department, Test, User, Order, Result, Login_Manager
from .databaseMangement.serializers import DepartmentSerializer, TestSerializer, UserSerializer, OrderSerializer, ResultSerializer, Login_ManagerSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .databaseMangement.customAuth import authenticate

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

# Department Table
def getDepartment(request,pk):
    try:
        dept=Department.objects.get(Department_ID=pk)
        serializer=DepartmentSerializer(dept)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def department(request):
    
    if request.method == 'GET':
        dept=Department.objects.all()
        serializer=DepartmentSerializer(dept, many=True, context={'request':request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Test Table
def getTest(request,pk):
    test=Test.objects.get(Test_ID=pk)
    serializer=TestSerializer(test)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['GET', 'POST'])
def test(request):
    
    if request.method == 'GET':
        dept=Test.objects.all()
        serializer=TestSerializer(dept, many=True, context={'request':request})
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Table
def getUser(request,pk):
    user=User.objects.get(User_ID=pk)
    serializer=UserSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['GET', 'POST'])
def user(request):
    
    if request.method == 'GET':
        dept=User.objects.all()
        serializer=UserSerializer(dept, many=True, context={'request':request})
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Order Table
def getOrder(request,pk):
    order=Order.objects.get(Order_ID=pk)
    serializer=OrderSerializer(order)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['GET', 'POST'])
def order(request):
    
    if request.method == 'GET':
        dept=Order.objects.all()
        serializer=OrderSerializer(dept, many=True, context={'request':request})
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Result Table
def getResult(request,pk):
    result=Result.objects.get(Result_ID=pk)
    serializer=ResultSerializer(result)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['GET', 'POST'])
def result(request):
    
    if request.method == 'GET':
        dept=Result.objects.all()
        serializer=ResultSerializer(dept, many=True, context={'request':request})
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Login_Manager Table
def getLogin_Manager(request,pk):
    login_Manager=Login_Manager.objects.get(Email_adress=pk)
    serializer=Login_ManagerSerializer(login_Manager)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


@api_view(['POST'])
def Login(request):
    
    if request.method == 'POST':
        Email_Address=request.data["Email_Address"]
        Password=request.data["Password"]
        try:
                user = Login_Manager.objects.get(Email_Address=Email_Address)
                if user.Password==Password:
                    serializer = Login_ManagerSerializer(user)
                    return Response(serializer.data)
                else:
                    Response(status=status.HTTP_206_PARTIAL_CONTENT)
        except Login_Manager.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        '''
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
        '''

def isNew_eMail(email):
    try:
        Login_Manager.objects.get(Email_Address=email)
        return False
    except Login_Manager.DoesNotExist:
        return True

@api_view(['POST'])
def SignUp(request):
    
    if request.method == 'POST':
        serializer = Login_ManagerSerializer(data=request.data)
        if serializer.is_valid():
            if(isNew_eMail(request.data["Email_Address"])):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
               return Response(status=status.HTTP_208_ALREADY_REPORTED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

