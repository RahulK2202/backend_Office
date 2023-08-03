from rest_framework import serializers
from .models import LeaveRequest
from adminapp.serializers import UserDataSerializer,DepartmentSerializer

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
 

class LeaveWithEmployeeSerializer(serializers.ModelSerializer):
    employee = UserDataSerializer()
    department = DepartmentSerializer(source='employee.department')  # Use source to access the department field in the Employee model

    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'department', 'leave_type', 'start_date', 'end_date', 'reason', 'is_approved']