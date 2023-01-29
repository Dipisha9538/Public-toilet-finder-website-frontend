# Generated by Django 4.1.5 on 2023-01-24 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostel_name', models.CharField(max_length=100)),
                ('Hostel_Address', models.CharField(max_length=50)),
                ('Hostel_Ph_No', models.PositiveIntegerField(blank=True, null=True)),
                ('Hostel_Mobile_No', models.CharField(blank=True, max_length=10, null=True)),
                ('Hostel_Price', models.PositiveIntegerField(blank=True, null=True)),
                ('Hostel_Estd', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date ESTD')),
                ('Hostel_lat', models.CharField(blank=True, max_length=250, null=True)),
                ('Hostel_long', models.CharField(blank=True, max_length=250, null=True)),
                ('Hostel_type', models.CharField(blank=True, max_length=250, null=True)),
                ('wifi', models.BooleanField(default=False)),
                ('lodging', models.BooleanField(default=False)),
                ('studyRoom', models.BooleanField(default=False)),
                ('laundary', models.BooleanField(default=False)),
                ('medicalFacility', models.BooleanField(default=False)),
                ('singleRoom', models.BooleanField(default=False)),
                ('dormitory', models.BooleanField(default=False)),
                ('about', models.TextField(blank=True, max_length=200)),
                ('user_ins', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostel_name', models.CharField(max_length=100)),
                ('Hostel_Address', models.CharField(max_length=50)),
                ('Hostel_Ph_No', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Hostel_Mobile_No', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('Hostel_Price', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Hostel_Estd', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date ESTD')),
                ('Hostel_lat', models.CharField(blank=True, max_length=250, null=True)),
                ('Hostel_long', models.CharField(blank=True, max_length=250, null=True)),
                ('Hostel_type', models.CharField(blank=True, max_length=250, null=True)),
                ('wifi', models.BooleanField(default=False)),
                ('lodging', models.BooleanField(default=False)),
                ('studyRoom', models.BooleanField(default=False)),
                ('laundary', models.BooleanField(default=False)),
                ('medicalFacility', models.BooleanField(default=False)),
                ('singleRoom', models.BooleanField(default=False)),
                ('dormitory', models.BooleanField(default=False)),
                ('about', models.TextField(blank=True, max_length=200)),
                ('user_ins', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('Hostel_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.hostel_request')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('Hostel_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.hostel_info')),
            ],
        ),
        migrations.CreateModel(
            name='Hostel_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('commenton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.hostel_info')),
            ],
        ),
    ]
