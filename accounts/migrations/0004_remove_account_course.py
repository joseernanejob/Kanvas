# Generated by Django 4.2.4 on 2023-08-25 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='course',
        ),
    ]
