# Generated by Django 5.1.2 on 2024-11-01 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('version', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TestSubject',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('successRate', models.FloatField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='ApertureScience.product')),
                ('testSubjects', models.ManyToManyField(related_name='experiments', to='ApertureScience.testsubject')),
            ],
        ),
    ]
