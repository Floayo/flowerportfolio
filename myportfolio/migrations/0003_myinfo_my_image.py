# Generated by Django 3.2.25 on 2025-04-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20250414_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='my_image',
            field=models.ImageField(blank=True, upload_to='My_img/'),
        ),
    ]
