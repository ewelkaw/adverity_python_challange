# Generated by Django 4.1.7 on 2023-02-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='')),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
