# Generated by Django 3.2.19 on 2023-07-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(default=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
