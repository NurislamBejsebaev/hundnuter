# Generated by Django 4.1.7 on 2023-08-08 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsview',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new', to='news.articlenew'),
        ),
    ]
