from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    
