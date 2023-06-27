# Generated by Django 3.2.19 on 2023-06-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField()),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-date_created'],
            },
        ),
    ]
