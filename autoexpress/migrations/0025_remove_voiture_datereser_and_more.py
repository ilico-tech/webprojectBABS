# Generated by Django 4.1.7 on 2023-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0024_alter_voiture_annee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voiture',
            name='Datereser',
        ),
        migrations.RemoveField(
            model_name='voiture',
            name='messageclient',
        ),
        migrations.RemoveField(
            model_name='voiture',
            name='nomclient',
        ),
        migrations.AlterField(
            model_name='voiture',
            name='prix',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]