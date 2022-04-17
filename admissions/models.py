from django.db import models
from django.urls import reverse,reverse_lazy
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=1000)
    father_Name = models.CharField(max_length=1000)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=1000)
    emailid = models.CharField(max_length=1000)




class StaffList(models.Model):
    name = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    phone_No = models.CharField(max_length=1000)
    experience = models.IntegerField()

    def get_absolute_url(self):
        return reverse('teachersList')
