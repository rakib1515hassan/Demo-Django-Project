from django import forms
from django.forms import (
    ModelForm, TextInput, Select, CheckboxInput, NumberInput, FileInput, SelectMultiple, Textarea, \
    PasswordInput, EmailInput
)

from django.contrib.auth import get_user_model
User = get_user_model()

from apps.student.models import Student



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'

        fields = ['name', 'roll', 'subject', 'description', 'image', 'cv']

        widgets = {
            'name' : TextInput( attrs={
                    'class': 'form-control',  
                    'placeholder': 'Write student name',
                    'required': True,
                }),

            'roll' : TextInput( attrs={
                    'class': 'form-control',  
                    'placeholder': 'Write student roll',
                    'required': True,
                }),

            'subject' : Select( attrs={
                    'class': 'form-select',  
                    'placeholder': 'select student subject',
                    'required': True,
                }),
            
            'image' : FileInput( attrs={
                    'class': 'form-control', 
                    'accept' : 'image/jpeg image/png image/jpg',
                    # 'style': 'border-style: dotted;',
                }),

            'cv' : FileInput( attrs={
                    'class': 'form-control', 
                    'accept' : '.pdf',
                    # 'style': 'border-style: dotted;',
                }),

            # 'dob': forms.DateInput(
            #         format=('%Y-%m-%d'),
            #         attrs={'class': 'form-control',
            #             'placeholder': 'Select Birthdate',
            #             'type': 'date'
            #     }),

            # 'email' : EmailInput(attrs={
            #         'class': 'form-control', 
            #         'placeholder': 'Enter Email',
            #         'required': True
            #     }),

            # 'phone' : TextInput( attrs={
            #         'class': 'form-control', 
            #         'placeholder': 'Enter Phone Number',
            #         'required': True
            #     }),

            
            
            # 'gender' : Select(attrs={
            #         'class': 'form-select js-choice', 
            #     }),
            
            # 'address' : Textarea(attrs={
            #         'class': 'form-select',
            #         'placeholder': 'Enter the address...',
            #         'rows':4,
            #         'cols':50, 
            #     }),

            # 'joining': forms.DateInput(
            #         format=('%Y-%m-%d'),
            #         attrs={'class': 'form-control',
            #             'placeholder': 'Select joining date...',
            #             'type': 'date'
            #     }),
            # 'user_salary': NumberInput(attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Enter the salary',
            #     }),
        }



