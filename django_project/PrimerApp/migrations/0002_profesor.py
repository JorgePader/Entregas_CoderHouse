# Generated by Django 5.0.3 on 2024-03-31 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
            ],
        ),
    ]
