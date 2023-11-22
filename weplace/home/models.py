from re import M
from django.db import models

# Create your models here.
class CompanyRegister(models.Model):
    company_name=models.CharField(max_length=100)
    regstart=models.DateField()
    regend=models.DateField()
    applyhere=models.URLField()

    def __str__(self):
        return self.company_name    

class Student(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    admissionNo=models.CharField(max_length=100)
    uniRegNo=models.CharField(max_length=100)
    phoneNo=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    tenthaggr=models.CharField(max_length=100)
    twelvethaggr=models.CharField(max_length=100)
    backlogs=models.CharField(max_length=100)
    cgpa=models.CharField(max_length=100)
    registered_on= models.DateField(auto_now=True)
    SearchableFields=['firstname','lastname','backlogs','department','cgpa','tenthaggr','twelvethaggr']
