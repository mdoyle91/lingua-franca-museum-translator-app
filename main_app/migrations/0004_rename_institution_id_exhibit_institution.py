# Generated by Django 5.1.4 on 2024-12-13 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_exhibit_exhibit_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibit',
            old_name='institution_id',
            new_name='institution',
        ),
    ]
