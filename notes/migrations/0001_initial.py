# Generated by Django 3.2.8 on 2021-12-30 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDate', models.DateField()),
                ('branch', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('notesFile', models.FileField(upload_to='')),
                ('fileType', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=10)),
                ('sendTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.person')),
            ],
        ),
    ]
