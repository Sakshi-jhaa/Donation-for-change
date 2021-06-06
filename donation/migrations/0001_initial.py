# Generated by Django 3.2.4 on 2021-06-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donor_name', models.CharField(max_length=100)),
                ('Number_of_items', models.IntegerField()),
                ('Items', models.CharField(max_length=100)),
                ('donation_date', models.DateField()),
                ('cash', models.IntegerField()),
            ],
        ),
    ]
