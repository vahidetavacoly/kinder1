# Generated by Django 4.2.14 on 2024-08-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panelapp', '0014_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='alt_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
