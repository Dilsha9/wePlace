# Generated by Django 4.1.1 on 2022-09-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
