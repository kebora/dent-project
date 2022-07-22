# Generated by Django 4.0.6 on 2022-07-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name_of_service',
            field=models.CharField(choices=[('GD', 'Graphic Design'), ('MG', 'Motion Graphics')], max_length=2, unique=True),
        ),
    ]