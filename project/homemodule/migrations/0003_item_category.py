# Generated by Django 3.1.7 on 2021-03-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemodule', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='gujarati', max_length=20),
        ),
    ]
