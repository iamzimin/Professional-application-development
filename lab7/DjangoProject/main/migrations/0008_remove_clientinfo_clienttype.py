# Generated by Django 4.1.6 on 2023-02-04 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_clientgroup_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientinfo',
            name='clientType',
        ),
    ]
