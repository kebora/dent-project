# Generated by Django 4.0.6 on 2022-07-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sketch',
            options={'verbose_name_plural': 'Sketches'},
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Description not added!'),
        ),
    ]
