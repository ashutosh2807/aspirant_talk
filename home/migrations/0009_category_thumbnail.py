# Generated by Django 4.1.6 on 2023-04-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_image_blog_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Cat_thumbnails'),
        ),
    ]
