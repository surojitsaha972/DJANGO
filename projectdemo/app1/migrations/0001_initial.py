# Generated by Django 5.0.1 on 2024-01-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
