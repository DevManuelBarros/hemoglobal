# Generated by Django 3.1.1 on 2020-09-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20200930_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fecha_turno',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
