# Generated by Django 3.2.19 on 2023-09-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cast',
        ),
        migrations.AddField(
            model_name='post',
            name='cast',
            field=models.TextField(blank=True),
        ),
    ]
