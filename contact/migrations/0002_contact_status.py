# Generated by Django 4.0.6 on 2022-07-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
