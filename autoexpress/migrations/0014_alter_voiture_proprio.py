# Generated by Django 4.1.7 on 2023-03-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0013_alter_voiture_proprio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='proprio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
