# Generated by Django 4.1 on 2022-08-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cricketmodel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cricket_team',
            },
        ),
        migrations.CreateModel(
            name='empmodel',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_course', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
