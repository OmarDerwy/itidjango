# Generated by Django 5.1.6 on 2025-02-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50, unique=True, verbose_name='Class name')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('year', models.IntegerField(verbose_name='Year')),
            ],
        ),
    ]
