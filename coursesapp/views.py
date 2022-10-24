from .models import Course
from .serializers import CourseSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

# Create your views here.

class CourseList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing courses.

    post:
    Create a new course instance.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the given course.

    delete:
    Delete the given user.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
