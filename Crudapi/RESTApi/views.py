from django.shortcuts import render

# Create your views here.
from .models import Employees,Inventory
from .serializers import EmployeesSerializer,InventorySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

class EmployeesTable(APIView):

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get(self,request):
        empobj = Employees.objects.all()
        empserializerobj = EmployeesSerializer(empobj,many=True)
        return Response(empserializerobj.data,status=status.HTTP_200_OK)

