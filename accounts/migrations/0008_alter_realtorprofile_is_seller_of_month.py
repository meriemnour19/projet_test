# Generated by Django 5.0.4 on 2024-04-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customerprofile_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtorprofile',
            name='is_seller_of_month',
            field=models.BooleanField(default=False),
        ),
    ]
