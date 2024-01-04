from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    is_activated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Lawyer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255)
    ratings = models.FloatField()
    age = models.IntegerField()
    experience = models.CharField(max_length=255)


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    needed_expertise = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
