# Generated by Django 2.2.6 on 2019-10-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
