# Generated by Django 3.2.19 on 2023-09-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20230927_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cast',
            field=models.ManyToManyField(blank=True, related_name='actor_list', to='blog.Actor'),
        ),
    ]
