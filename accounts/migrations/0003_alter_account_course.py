# Generated by Django 4.2.4 on 2023-08-25 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_instructor'),
        ('students_courses', '0001_initial'),
        ('accounts', '0002_account_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='course',
            field=models.ManyToManyField(related_name='student', through='students_courses.StudentCourse', to='courses.course'),
        ),
    ]
