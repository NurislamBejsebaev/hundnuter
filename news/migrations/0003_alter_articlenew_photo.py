# Generated by Django 4.1.7 on 2023-08-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_profile_photo_articlenew_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlenew',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/', verbose_name='ФОТО новостей'),
        ),
    ]