# Generated by Django 5.0.3 on 2024-04-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='image',
            field=models.ImageField(upload_to='announce/%y/%m/%d'),
        ),
    ]