# Generated by Django 3.1.2 on 2020-11-07 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date'),
        ),
    ]
