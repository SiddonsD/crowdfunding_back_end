# Generated by Django 4.2.3 on 2024-02-29 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
