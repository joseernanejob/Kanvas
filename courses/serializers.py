from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentsCourseSerializer, NewStudentsSerializer
from .utils import verifyStudent


class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentsCourseSerializer(
        many=True, source="students", read_only=True
    )

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        read_only_fields = ["contents"]


class CourseStudentsSerializer(serializers.ModelSerializer):
    students_courses = NewStudentsSerializer(many=True, read_only=True)

    def update(self, instance: Course, validated_data: dict):
        students = self.initial_data["students_courses"]
        invalidStudents = verifyStudent(instance, students)

        if len(invalidStudents) > 0:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(invalidStudents)}."
                }
            )

        instance.save()
        return instance

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["name"]
