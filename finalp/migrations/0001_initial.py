# Generated by Django 3.1.5 on 2021-01-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
                ('user_name', models.CharField(max_length=10)),
                ('password', models.IntegerField()),
            ],
        ),
    ]