from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rollno=models.CharField(max_length=10,default="null")
    contact=models.CharField(max_length=10,default="null")
    batch=models.CharField(max_length=4,default="null")
    branch=models.CharField(max_length=30,default="null")
    section=models.CharField(max_length=1,default="n")

    def __str__(self):
        return str(self.pk)

class Notes(models.Model):
    user=models.ForeignKey(Person,on_delete=models.CASCADE)
    uploadDate=models.CharField(max_length=20,default="null")
    subject=models.CharField(max_length=30,default="null")
    semester=models.CharField(max_length=1,default=0)
    notesFile=models.FileField()
    fileType=models.CharField(max_length=10,default="null")
    description=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=10,default="null")
    receiverType=models.CharField(max_length=7,default="null")
    sendTo=models.CharField(max_length=40,default="null")

    def __str__(self):
        return str(self.pk)

class Contact(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id