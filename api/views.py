from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer
from mainapp.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_students(request):
    get_all_students = Student.objects.all()
    serializer = StudentSerializer(get_all_students, many=True)
    return Response(serializer.data)
    