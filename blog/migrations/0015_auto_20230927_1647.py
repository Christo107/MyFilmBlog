# Generated by Django 3.2.19 on 2023-09-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20230924_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='films',
        ),
        migrations.AddField(
            model_name='actor',
            name='posts',
            field=models.ManyToManyField(blank=True, to='blog.Post'),
        ),
    ]
