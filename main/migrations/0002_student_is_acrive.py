# Generated by Django 5.0.7 on 2024-08-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_acrive',
            field=models.BooleanField(default=True, verbose_name='learning'),
        ),
    ]
