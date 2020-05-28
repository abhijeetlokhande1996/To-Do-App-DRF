# Generated by Django 3.0.5 on 2020-05-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('isComplete', models.BooleanField()),
                ('scheduleTime', models.DateTimeField()),
            ],
        ),
    ]
