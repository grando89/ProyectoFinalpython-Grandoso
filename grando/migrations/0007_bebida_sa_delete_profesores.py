# Generated by Django 5.0.2 on 2024-03-08 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grando', '0006_vinos_delete_alumnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida_sa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profesores',
        ),
    ]
