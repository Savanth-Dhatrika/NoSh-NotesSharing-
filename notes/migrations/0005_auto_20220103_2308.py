# Generated by Django 3.2.8 on 2022-01-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_person_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='branch',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='uploadDate',
            field=models.CharField(max_length=20, null=True),
        ),
    ]