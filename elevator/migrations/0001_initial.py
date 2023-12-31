# Generated by Django 4.2.4 on 2023-08-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('elevator_name', models.CharField(max_length=10, unique=True)),
                ('current_floor', models.PositiveIntegerField(choices=[(1, '1st Floor'), (2, '2nd Floor'), (3, '3rd Floor'), (4, '4th Floor'), (5, '5th Floor')], default=1)),
                ('is_operational', models.BooleanField(default=True)),
                ('is_available', models.BooleanField(default=True)),
                ('is_busy', models.BooleanField(default=False)),
                ('is_under_maintenance', models.BooleanField(default=False)),
                ('is_moving_up', models.BooleanField(default=True)),
                ('is_moving_down', models.BooleanField(default=False)),
                ('is_door_open', models.BooleanField(default=False)),
                ('is_door_closed', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Elevator',
            },
        ),
        migrations.CreateModel(
            name='ElevatorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_floor', models.PositiveIntegerField(choices=[(1, '1st Floor'), (2, '2nd Floor'), (3, '3rd Floor'), (4, '4th Floor'), (5, '5th Floor')], default=1)),
                ('request_status', models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=20)),
            ],
            options={
                'db_table': 'ElevatorRequest',
            },
        ),
        migrations.CreateModel(
            name='FloorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requested_floor', models.PositiveIntegerField(choices=[(1, '1st Floor'), (2, '2nd Floor'), (3, '3rd Floor'), (4, '4th Floor'), (5, '5th Floor')])),
                ('request_status', models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=20)),
            ],
            options={
                'db_table': 'FloorRequest',
            },
        ),
    ]
