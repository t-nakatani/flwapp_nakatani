# Generated by Django 4.0.4 on 2022-05-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_imagemodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='gray',
            field=models.ImageField(default='Not Set', upload_to=''),
        ),
    ]
