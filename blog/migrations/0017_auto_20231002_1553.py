# Generated by Django 3.2.19 on 2023-10-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_cast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.ManyToManyField(blank=True, to='blog.Genre'),
        ),
    ]