# Generated by Django 2.0.6 on 2018-07-06 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0010_auto_20180706_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidding',
            old_name='c_id',
            new_name='com_id',
        ),
    ]
