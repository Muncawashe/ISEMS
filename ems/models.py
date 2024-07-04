from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class User(AbstractUser):
    phone = models.IntegerField(default=0, null=True, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="dept", default=1)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name="role", default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Events(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tableevents"
