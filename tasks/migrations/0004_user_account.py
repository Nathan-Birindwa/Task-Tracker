# Generated by Django 4.2.4 on 2024-02-29 20:16

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=100, verbose_name=tasks.models.Task)),
            ],
        ),
    ]
