# Generated by Django 3.2.6 on 2024-06-27 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
                ('activity_description', models.TextField()),
                ('activity_date', models.DateField()),
                ('activity_time', models.TimeField()),
                ('activity_max_grade', models.FloatField()),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_grade', models.FloatField(default=0.0)),
                ('answer', models.TextField()),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assignments.activity')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
