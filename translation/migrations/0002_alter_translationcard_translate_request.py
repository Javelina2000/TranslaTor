# Generated by Django 4.1.5 on 2023-01-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationcard',
            name='translate_request',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]