# Generated by Django 2.2.12 on 2020-05-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assign_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='assignment date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='code_coins',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='finish date'),
        ),
    ]
