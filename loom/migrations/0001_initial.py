# Generated by Django 3.2 on 2025-06-17 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LoomVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('transcript', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loom.user')),
            ],
        ),
    ]
