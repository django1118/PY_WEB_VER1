# Generated by Django 3.1.2 on 2020-10-24 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date'),
        ),
    ]
