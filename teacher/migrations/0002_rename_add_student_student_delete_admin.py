# Generated by Django 4.1.2 on 2022-11-30 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_Student',
            new_name='Student',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
