# Generated by Django 3.2.19 on 2023-06-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='films',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
