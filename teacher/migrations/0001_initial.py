# Generated by Django 5.1 on 2024-09-13 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('birthday', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('url_picture', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('available', models.BooleanField(default=False)),
                ('speciality', models.CharField(max_length=20)),
                ('adress', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_address', to='base.adressmodel')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
