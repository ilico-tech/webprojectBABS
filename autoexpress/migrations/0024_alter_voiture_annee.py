# Generated by Django 4.1.7 on 2023-04-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0023_alter_voiture_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='annee',
            field=models.DateField(blank=True, null=True),
        ),
    ]
