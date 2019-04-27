# Generated by Django 2.2 on 2019-04-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('departure_from', models.CharField(max_length=100)),
                ('departure_to', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('nid', models.IntegerField()),
                ('profession', models.CharField(max_length=50)),
                ('blood_group', models.CharField(choices=[(1, 'A+'), (2, 'B+'), (3, 'O+'), (4, 'AB+'), (5, 'A-'), (6, 'B-'), (7, 'O-'), (8, 'AB-')], default=1, max_length=1)),
                ('present_address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Islamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[(1, 'Hazz'), (2, 'Umrah')], default=1, max_length=1)),
                ('places', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=3)),
                ('members', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[(1, 'Normal Tour'), (2, 'Oficial Tour'), (3, 'Honeymoon')], default=1, max_length=1)),
                ('places', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=3)),
                ('members', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('processing_time', models.CharField(max_length=30)),
            ],
        ),
    ]
