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
    hours_worked = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    
    def __str__(self):
        return f"Session for {self.user.username}"
    
class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Leave application for {self.user.username}"
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    end = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    perfomance = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    msg = models.TextField()
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg