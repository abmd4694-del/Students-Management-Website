from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Student
from .serializers import StudentSerializer

class StudentListAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'department']
    ordering_fields = ['name', 'age']

class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
