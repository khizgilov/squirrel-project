# Generated by Django 3.1.2 on 2020-10-16 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelSighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=500, unique=True)),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('longitude', models.FloatField(help_text='Longitude')),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='AM or PM', max_length=2)),
                ('date', models.DateField(help_text='Date of sighting')),
                ('age', models.CharField(blank=True, help_text='Age description', max_length=100)),
            ],
        ),
    ]
