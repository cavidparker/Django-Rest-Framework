# Generated by Django 3.1.3 on 2021-01-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multiple_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title_english', models.CharField(max_length=200)),
                ('page_title_bangla', models.CharField(max_length=200)),
                ('page_template_english', models.CharField(max_length=200)),
                ('page_template_bangla', models.CharField(max_length=200)),
                ('page_heading_english', models.CharField(max_length=200)),
                ('page_heading_bangla', models.CharField(max_length=200)),
                ('play', models.ManyToManyField(blank=True, related_name='play_page', to='Multiple_model.Play')),
                ('poem', models.ManyToManyField(blank=True, related_name='poem_page', to='Multiple_model.Poem')),
            ],
        ),
    ]
