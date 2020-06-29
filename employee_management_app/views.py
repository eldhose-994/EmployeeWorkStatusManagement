from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from employee_management_app.models import EmployeeTasks
from employee_management_app.serializers import EmployeeDailyStatusSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user_obj)
        return Response({
            'token': token.key,
            'user_id': user_obj.pk,
            'email': user_obj.email
        })


class EmployeeTaskView(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to view or edit taks.
    """
    serializer_class = EmployeeDailyStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tasks_obj = EmployeeTasks.objects.filter(employee=self.request.user.id).order_by('-created_at')
        print(tasks_obj)
        return tasks_obj
