# Generated by Django 3.1.3 on 2021-01-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multiple_model', '0003_delete_maindetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='our_value_image')),
                ('image_sd', models.ImageField(upload_to='our_value_image_sd')),
            ],
        ),
    ]