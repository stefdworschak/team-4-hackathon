# Generated by Django 4.0 on 2021-12-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0003_alter_date_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='calendar',
            name='year',
            field=models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)], default=2021),
        ),
    ]
