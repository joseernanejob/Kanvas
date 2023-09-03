from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .serializers import CourseSerializer, CourseStudentsSerializer
from .models import Course
from accounts.permissions import isAdmin
from students_courses.models import StudentCourse


class CourseView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "id_course"


class CourseStudentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]
    queryset = Course.objects.all()
    serializer_class = CourseStudentsSerializer
    lookup_url_kwarg = "id_course"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, id_student, id_course):
        try:
            student = StudentCourse.objects.get(
                student_id=id_student, course_id=id_course
            )
            student.delete()
        except:
            return Response(
                data={"detail": "this id is not associated with this course."},
                status=404,
            )
        return Response(status=HTTP_204_NO_CONTENT)
