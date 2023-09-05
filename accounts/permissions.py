from rest_framework import permissions
from rest_framework.views import View
from courses.models import Course


class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class isStudentCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = Course.objects.get(pk=obj.course_id)
        is_valid = course.students.contains(request.user)
        return is_valid or request.user.is_authenticated and request.user.is_superuser
