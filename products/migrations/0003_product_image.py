# Generated by Django 3.0.7 on 2020-06-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200629_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='python.png', upload_to='profile_pic'),
        ),
    ]
