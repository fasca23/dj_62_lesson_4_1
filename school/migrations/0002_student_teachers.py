# Generated by Django 4.1.5 on 2023-01-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='student', through='school.Teacher_Student', to='school.teacher'),
        ),
    ]
