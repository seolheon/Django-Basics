# Generated by Django 5.0.4 on 2024-04-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Записка',
                'verbose_name_plural': 'Записки',
            },
        ),
    ]
