# Generated by Django 2.0.6 on 2018-09-29 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180929_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='i_barcode',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='i_fam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i_fam_id', to='mainapp.Family'),
        ),
    ]