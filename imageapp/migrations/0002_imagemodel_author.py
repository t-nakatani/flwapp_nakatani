# Generated by Django 4.0.4 on 2022-05-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
