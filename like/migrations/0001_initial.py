# Generated by Django 2.2 on 2020-02-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=25)),
                ('password', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=25)),
            ],
        ),
    ]
