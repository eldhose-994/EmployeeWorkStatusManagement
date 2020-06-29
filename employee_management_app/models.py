from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class EmployeeTasks(models.Model):
    TASK_STATUS = (('0', 'New'),
                   ('1', 'In Progress'),
                   ('2', 'Completed'))
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Task Name'), max_length=100)
    description = models.CharField(_('Description'), max_length=200, null=True, blank=True)
    status = models.CharField(_('Task Status'), max_length=1, choices=TASK_STATUS, default="0")
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())
