# Generated by Django 4.0.6 on 2022-07-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('Resolved', 'Resolved'), ('Not resolved', 'Not resolved')], max_length=100),
        ),
    ]
