# Generated by Django 5.1.2 on 2024-11-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApertureScience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubject',
            name='surname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
