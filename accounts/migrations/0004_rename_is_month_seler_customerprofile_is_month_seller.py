# Generated by Django 5.0.3 on 2024-04-02 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customerprofile_is_month_seler'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='is_month_seler',
            new_name='is_month_seller',
        ),
    ]