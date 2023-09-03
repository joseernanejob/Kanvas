from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Course
from .serializers import ContentSerializer
from accounts.permissions import isAdmin

# Create your views here.


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]
    serializer_class = ContentSerializer

    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs.get("id_course"))

    def perform_create(self, serializer):
        return serializer.save(course=self.get_course())
