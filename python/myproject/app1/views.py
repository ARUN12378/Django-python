from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# CREATE student
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# READ all students
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# READ single student
@api_view(['GET'])
def get_student(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


# UPDATE student
@api_view(['PUT'])
def update_student(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# DELETE student
@api_view(['DELETE'])
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message": "Student deleted"})
