# Generated by Django 3.2.8 on 2022-01-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20220106_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('msgdate', models.DateField(null=True)),
                ('isread', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.CharField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='section',
            field=models.CharField(default='n', max_length=1),
        ),
    ]
