# Generated by Django 4.1.7 on 2023-05-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0031_alter_voiture_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='boitevitesse',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='categorie',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]