# Generated by Django 4.1.6 on 2023-03-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Thumbnails'),
        ),
    ]
