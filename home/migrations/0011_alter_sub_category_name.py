# Generated by Django 4.1.6 on 2023-04-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]