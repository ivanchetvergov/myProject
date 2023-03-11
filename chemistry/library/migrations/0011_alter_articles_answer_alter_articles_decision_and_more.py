# Generated by Django 4.1.5 on 2023-03-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_articles_decision_alter_articles_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='answer',
            field=models.CharField(max_length=250, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='decision',
            field=models.TextField(default='Решение: ', verbose_name='Решение'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='shorts',
            field=models.CharField(default='Урок Задание ', max_length=250, verbose_name='Название'),
        ),
    ]
