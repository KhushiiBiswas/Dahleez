# Generated by Django 3.1.5 on 2022-02-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_campaign'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Campaign',
        ),
        migrations.DeleteModel(
            name='FocusArea',
        ),
    ]
