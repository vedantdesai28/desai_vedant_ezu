# Generated by Django 3.2.12 on 2022-02-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_number', 'course_name']},
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('course_number', 'course_name'), name='unique_course'),
        ),
    ]
