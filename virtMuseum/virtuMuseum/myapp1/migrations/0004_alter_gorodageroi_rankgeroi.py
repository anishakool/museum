# Generated by Django 5.0.6 on 2024-06-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_alter_gorodageroi_rankgeroi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gorodageroi',
            name='rankGeroi',
            field=models.CharField(blank=True, db_default='Город-герой', max_length=30),
        ),
    ]