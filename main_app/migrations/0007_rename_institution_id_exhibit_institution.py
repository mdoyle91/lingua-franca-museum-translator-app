# Generated by Django 5.1.4 on 2024-12-16 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_institution_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibit',
            old_name='institution_id',
            new_name='institution',
        ),
    ]
