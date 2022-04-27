from django import forms
from .models import Student , Track
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname' , 'lname' , 'age' , 'student_track')

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name' ,)        