# Generated by Django 4.0.5 on 2023-01-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SQLServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('server_id', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
