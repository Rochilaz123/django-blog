# Generated by Django 4.2.13 on 2024-06-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
