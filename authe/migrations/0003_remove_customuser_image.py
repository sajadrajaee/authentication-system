# Generated by Django 4.2.6 on 2024-07-06 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0002_alter_customuser_email_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]
