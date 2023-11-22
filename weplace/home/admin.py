from typing import Sequence
from django.contrib import admin
from .models import CompanyRegister,Student
# Register your models here.
admin.site.register(CompanyRegister)

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','admissionNo','uniRegNo','phoneNo','email','dob','gender','semester','department','tenthaggr','twelvethaggr','backlogs','cgpa','registered_on')
    list_filter=['backlogs','cgpa','department','tenthaggr','twelvethaggr']
    search_fields=Student.SearchableFields
admin.site.register(Student,StudentAdmin)
