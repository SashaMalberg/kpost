# Generated by Django 2.2 on 2020-02-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0003_posts_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
