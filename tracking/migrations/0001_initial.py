# Generated by Django 4.2.5 on 2023-10-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DockerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
