from django.urls import path

from .views import CourseView, CourseDetailView, CourseStudentView
from contents.views import ContentView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<str:id_course>/", CourseDetailView.as_view()),
    path("courses/<str:id_course>/contents/", ContentView.as_view()),
    path("courses/<str:id_course>/students/", CourseStudentView.as_view()),
    path("courses/<str:id_course>/contents/", ContentView.as_view()),
    path(
        "courses/<str:id_course>/students/<str:id_student>/",
        CourseStudentView.as_view(),
    ),
]
