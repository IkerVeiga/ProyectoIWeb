# Generated by Django 5.1.2 on 2024-11-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApertureScience', '0002_alter_testsubject_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]
