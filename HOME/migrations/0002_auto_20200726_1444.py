# Generated by Django 3.0.4 on 2020-07-26 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammembers',
            old_name='Thought',
            new_name='linkedinid',
        ),
        migrations.RenameField(
            model_name='teammembers',
            old_name='linedinid',
            new_name='thought',
        ),
    ]
