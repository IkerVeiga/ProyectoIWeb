# Generated by Django 5.1.2 on 2024-10-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApertureScience', '0002_product_description_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsubject',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testsubject',
            name='number',
            field=models.IntegerField(),
        ),
    ]
