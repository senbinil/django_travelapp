# Generated by Django 3.2.7 on 2021-09-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_module', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
