# Generated by Django 4.1.1 on 2022-09-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('regstart', models.DateField()),
                ('regend', models.DateField()),
                ('applyhere', models.TextField()),
            ],
        ),
    ]
