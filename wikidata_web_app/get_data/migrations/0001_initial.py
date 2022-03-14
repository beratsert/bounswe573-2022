# Generated by Django 4.0.3 on 2022-03-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=2)),
            ],
        ),
    ]
