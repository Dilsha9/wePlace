from msilib.schema import RadioButton
from random import choices
from secrets import choice
from socket import fromshare
from django import forms
from .models import Student

    
    

class DateInput(forms.DateInput):
    input_type='date'
class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= '__all__'

        widgets={
            'dob': DateInput(),
        
        }
        labels ={
        'firstname': "First Name:",
        'lastname': "Last Name:",
        'admissionNo': "Admission Number:",
        'uniRegNo': "University Register Number:",
        'phoneNo': "Phone Number:",
        'email': "Email:",
        'dob': "Date Of Birth",
        'gender': "Gender",
        'semester': "Semester",
        'department': "Department",
        'tenthaggr': "10th Aggregate:",
        'twelvethaggr': "12th/Diploma Aggregate",
        'backlogs': "Backlogs:",
        'cgpa': "CGPA(till the current semester):"
    
        }