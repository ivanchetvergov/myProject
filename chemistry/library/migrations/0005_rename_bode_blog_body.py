# Generated by Django 4.1.5 on 2023-01-18 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='bode',
            new_name='body',
        ),
    ]
