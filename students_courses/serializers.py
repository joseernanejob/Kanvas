from rest_framework import serializers

from .models import StudentCourse


class StudentsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = "__all__"
        depth = 1


class NewStudentsSerializer(serializers.ModelSerializer):
    student_email = serializers.SerializerMethodField("get_email")
    student_username = serializers.SerializerMethodField("get_name")

    def get_email(self, obj):
        return obj.student.email

    def get_name(self, obj):
        return obj.student.username

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]
