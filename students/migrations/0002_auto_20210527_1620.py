# Generated by Django 3.1.3 on 2021-05-27 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sections.section'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='identity_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]