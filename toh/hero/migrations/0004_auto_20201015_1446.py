# Generated by Django 3.1.2 on 2020-10-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20201015_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='age',
            field=models.IntegerField(default=25),
        ),
    ]
