# Generated by Django 5.0.3 on 2024-04-04 09:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_alter_customerprofile_status'),
        ('listings', '0006_annonce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('consultation_date', models.DateField(default=django.utils.timezone.now)),
                ('is_reviewed', models.BooleanField()),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('reponse_status', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customerprofile')),
                ('real_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('transaction_type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('CASH', 'CASH'), ('CARD', 'CARD')], max_length=100)),
                ('price', models.FloatField()),
                ('payment_status', models.CharField(max_length=100)),
                ('commission', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customerprofile')),
                ('realstor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.realtorprofile')),
            ],
        ),
    ]