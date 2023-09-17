# Generated by Django 4.2.4 on 2023-09-17 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0003_livedata_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
