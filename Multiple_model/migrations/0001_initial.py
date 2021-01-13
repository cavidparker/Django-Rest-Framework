# Generated by Django 3.1.3 on 2021-01-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=100)),
                ('lines', models.IntegerField()),
                ('stanzas', models.IntegerField()),
            ],
        ),
    ]
