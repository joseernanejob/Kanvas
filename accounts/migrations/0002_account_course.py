# Generated by Django 4.2.4 on 2023-08-25 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_instructor'),
        ('students_courses', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='course',
            field=models.ManyToManyField(related_name='account', through='students_courses.StudentCourse', to='courses.course'),
        ),
    ]
