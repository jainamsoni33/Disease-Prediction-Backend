# Generated by Django 2.1.4 on 2019-04-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20190411_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
