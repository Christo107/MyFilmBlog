# Generated by Django 3.2.19 on 2023-06-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cast',
            field=models.TextField(blank=True),
        ),
    ]
