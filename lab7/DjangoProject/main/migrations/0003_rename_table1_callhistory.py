# Generated by Django 4.1.6 on 2023-02-03 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_table1_options_table1_bankid_table1_clientid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table1',
            new_name='CallHistory',
        ),
    ]
