# Generated by Django 4.1.5 on 2023-01-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_rename_bode_blog_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('mean', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='shorts',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]