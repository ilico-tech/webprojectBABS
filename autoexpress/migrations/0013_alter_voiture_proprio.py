# Generated by Django 4.1.7 on 2023-03-28 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoexpress', '0012_alter_voiture_proprio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='proprio',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]