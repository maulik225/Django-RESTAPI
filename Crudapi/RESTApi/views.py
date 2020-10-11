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

@csrf_exempt
@permission_classes([IsAuthenticated])
class EmployeesTable(APIView):

    def get(self,request):
        empobj = Employees.objects.all()
        empserializerobj = EmployeesSerializer(empobj,many=True)
        return Response(empserializerobj.data,status=status.HTTP_200_OK)

    def post(self,request):
        try:
            empserializerobj = EmployeesSerializer(data=request.data)
            if empserializerobj.is_valid():
                empserializerobj.save()
                return Response(empserializerobj.data,status=status.HTTP_201_CREATED)
        except Exception:
            return Response(empserializerobj.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
@csrf_exempt
@permission_classes([IsAuthenticated])
class EmpUpdatedel(APIView):

    def get_object(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        empobj = self.get_object(pk)
        empserializeobj = EmployeesSerializer(empobj)
        return Response(empserializeobj.data)

    def put(self,request,pk):
        empobj = self.get_object(pk)
        empserializeobj = EmployeesSerializer(empobj,data=request.data)
        if empserializeobj.is_valid():
            empserializeobj.save()
            return Response(empserializeobj.data,status=status.HTTP_201_CREATED)
        return Response(empserializeobj.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk):
        empobj = self.get_object(pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

