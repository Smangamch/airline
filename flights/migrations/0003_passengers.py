# Generated by Django 4.2.11 on 2024-05-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_alter_flights_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flights')),
            ],
        ),
    ]