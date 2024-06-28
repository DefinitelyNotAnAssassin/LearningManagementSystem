# Generated by Django 3.2.6 on 2024-06-27 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('enrolled_students', models.ManyToManyField(related_name='enrolled_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=100)),
                ('material_description', models.TextField()),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
            ],
        ),
    ]
