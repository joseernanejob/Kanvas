from .models import Course
from accounts.models import Account


def verifyStudent(instance: Course, students):
    invalidStudent = []
    for studentInfo in students:
        email = studentInfo["student_email"]
        try:
            student = Account.objects.get(email=email)
            instance.students.add(student)
        except:
            invalidStudent.append(email)

    return invalidStudent
