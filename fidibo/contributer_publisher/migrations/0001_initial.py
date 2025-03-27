# Generated by Django 5.1.7 on 2025-03-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ebooks', models.TextField()),
                ('audiobooks', models.TextField()),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ebooks', models.TextField()),
                ('audiobooks', models.TextField()),
                ('magazines', models.TextField(blank=True, null=True)),
                ('biography', models.TextField()),
            ],
        ),
    ]
