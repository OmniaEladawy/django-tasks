from rest_framework import serializers
from .models import Student , Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('fname' , 'lname' , 'age' , 'student_track')
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep ['student_track'] = instance.student_track.track_name
        return rep

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'     