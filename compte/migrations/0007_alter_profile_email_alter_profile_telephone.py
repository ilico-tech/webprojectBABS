# Generated by Django 4.1.7 on 2023-04-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]