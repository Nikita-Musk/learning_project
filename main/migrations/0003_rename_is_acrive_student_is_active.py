# Generated by Django 5.0.7 on 2024-08-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_is_acrive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_acrive',
            new_name='is_active',
        ),
    ]
