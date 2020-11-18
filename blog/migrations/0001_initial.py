# Generated by Django 3.1.2 on 2020-11-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(blank=True, help_text='simple description', max_length=100, verbose_name='Description')),
            ],
        ),
    ]
