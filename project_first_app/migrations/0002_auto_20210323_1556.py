# Generated by Django 3.1.7 on 2021-03-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
