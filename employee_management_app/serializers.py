from rest_framework import serializers

from employee_management_app.models import EmployeeTasks


class EmployeeDailyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTasks
        fields = '__all__'
        read_only_fields = ['created_at', 'modified_at']
