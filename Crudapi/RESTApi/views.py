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

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def post(self,request):
        try:
            empserializerobj = EmployeesSerializer(data=request.data)
            if empserializerobj.is_valid():
                empserializerobj.save()
                return Response(empserializerobj.data,status=status.HTTP_201_CREATED)
        except Exception:
            return Response(empserializerobj.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmpUpdatedel(APIView):

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get_object(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get(self,request,pk):
        empobj = self.get_object(pk)
        empserializeobj = EmployeesSerializer(empobj)
        return Response(empserializeobj.data)
    
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def put(self,request,pk):
        empobj = self.get_object(pk)
        empserializeobj = EmployeesSerializer(empobj,data=request.data)
        if empserializeobj.is_valid():
            empserializeobj.save()
            return Response(empserializeobj.data,status=status.HTTP_201_CREATED)
        return Response(empserializeobj.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def delete(self,request,pk):
        empobj = self.get_object(pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InventoryTable(APIView):

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get(self,request):
        Invobj = Inventory.objects.all()
        invserializerobj = InventorySerializer(Invobj,many=True)
        return Response(invserializerobj.data)
    
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def post(self,request):
        Invserializerobj = InventorySerializer(data=request.data)
        if Invserializerobj.is_valid():
            Invserializerobj.save()
            return Response(Invserializerobj.data,status=status.HTTP_201_CREATED)
        return Response(Invserializerobj.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InvUpdatedel(APIView):
    
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get_object(self,pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def get(self,request,pk):
        invobj = self.get_object(pk)
        serializerobj = InventorySerializer(invobj)
        return Response(serializerobj.data)
    
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def put(self,request,pk):
        invobj = self.get_object(pk)
        invserializerobj = InventorySerializer(invobj,data=request.data)
        if invserializerobj.is_valid():
            invserializerobj.save()
            return Response(invserializerobj.data,status=status.HTTP_200_OK)
        # print("problem is here")
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def delete(self,request,pk):
        invobj = self.get_object(pk)
        invobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)