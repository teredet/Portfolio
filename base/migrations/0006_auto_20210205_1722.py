# Generated by Django 2.2 on 2021-02-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210205_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='images', verbose_name='Image'),
        ),
    ]
