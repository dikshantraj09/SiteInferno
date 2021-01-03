from django.db import models
# Create your models here.
class TeamMembers(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    imageprofile=models.ImageField(upload_to='shop/images', default="")
    linkedinid=models.CharField(max_length=100)
    thought=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=5000, default="")


    def __str__(self):
        return self.name

class Sponsor(models.Model):
    sponsorid=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='sponsor/images', default="")
    name=models.TextField(max_length=200)

