# Generated by Django 4.1.6 on 2023-02-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_bank_bankname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientgroup',
            name='type',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
    ]