# Generated by Django 4.1.5 on 2023-01-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('full', models.TextField(verbose_name='Описание')),

            ],
            options={
                'verbose_name': 'библиотека',
                'verbose_name_plural': 'Библиотека',
            },
        ),
        migrations.DeleteModel(
            name='Artiles',
        ),
    ]
