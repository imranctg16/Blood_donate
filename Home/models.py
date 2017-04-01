from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User  # for using the USer one to one model



# Create your models here.
class Division(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return  self.name

class Blood_group(models.Model):
    group=models.CharField(max_length=10)
    def __str__(self):
        return  self.group


def to_ (instance,filename):
    return "%s/%s"%(instance.user,filename)

class data(models.Model):
    user=models.ForeignKey(User)
    division=models.ForeignKey(Division)
    blood_group=models.ForeignKey(Blood_group)
    phone_number=models.CharField(max_length=11)
    image=models.ImageField(upload_to=to_,null=False ,blank=True)
    def __str__(self):
        return  self.user.username

#user class
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #comes up with some basic attributes(username,passward,email)
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    def __str__(self):
        return self.user.username