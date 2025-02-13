# Generated by Django 4.2.14 on 2024-08-20 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panelapp', '0009_image_modelcategory_delete_post_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.ImageField(upload_to='files/images')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panelapp.modelcategory')),
            ],
        ),
    ]
