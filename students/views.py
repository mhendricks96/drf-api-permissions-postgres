from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class StudentList(generics.ListAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer

class StudentList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


# class StudentDetail(generics.RetrieveAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer

# class StudentDetail(generics.RetrieveUpdateAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
