from rest_framework import serializers
from . models import Employees,Inventory

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmpId','name','emailID','contactNo','department')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'