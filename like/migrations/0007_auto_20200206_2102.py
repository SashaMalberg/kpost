# Generated by Django 2.2 on 2020-02-06 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0006_auto_20200205_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='login',
            new_name='uid',
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='like.Posts')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='like.Users')),
            ],
            options={
                'verbose_name': 'Голос',
                'verbose_name_plural': 'Голоса',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=255)),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='like.Posts')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='like.Users')),
            ],
        ),
    ]
