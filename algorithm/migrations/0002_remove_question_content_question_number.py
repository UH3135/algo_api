# Generated by Django 5.1.7 on 2025-03-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
