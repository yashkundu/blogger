# Generated by Django 3.0.4 on 2020-03-30 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20200330_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='author',
        ),
    ]