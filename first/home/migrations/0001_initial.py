# Generated by Django 4.1.5 on 2023-02-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]
