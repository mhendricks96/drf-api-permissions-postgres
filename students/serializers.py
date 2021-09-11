from rest_framework import serializers
from.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'birth_date', 'major', 'graduation_date', 'admitted_by')
    model = Student