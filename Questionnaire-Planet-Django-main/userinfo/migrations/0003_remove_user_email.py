# Generated by Django 3.2.23 on 2023-12-07 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20231130_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]