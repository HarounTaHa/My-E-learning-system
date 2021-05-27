# Generated by Django 3.1.3 on 2021-05-27 13:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('teachers', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=120)),
                ('number_of_question', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
                ('quiz_date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='quiz_date_created')),
                ('time', models.IntegerField(help_text='duration of the quiz in minute')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.section')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
