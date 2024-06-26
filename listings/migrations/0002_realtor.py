# Generated by Django 5.0.3 on 2024-04-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='realtors/%Y/%m/%d/')),
                ('biographie', models.TextField()),
                ('is_seller_of_month', models.BooleanField()),
                ('affiliation_date', models.DateField()),
                ('datetimefield', models.DateTimeField()),
            ],
        ),
    ]
