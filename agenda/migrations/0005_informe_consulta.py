# Generated by Django 3.1.1 on 2020-10-05 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20200930_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='informe_consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('observaciones', models.CharField(max_length=250)),
                ('turno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.turno')),
            ],
        ),
    ]