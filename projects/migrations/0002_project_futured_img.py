# Generated by Django 3.1.2 on 2023-02-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='futured_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]