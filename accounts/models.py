from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class User(AbstractUser):
    groupcolor = models.CharField(max_length=100)
    introduction = models.TextField()
    following = models.ManyToManyField("self", symmetrical=False,related_name="follower")
    profileimage = models.ImageField(blank=True, upload_to="profileimg")

 