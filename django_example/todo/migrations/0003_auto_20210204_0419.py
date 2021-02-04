# Generated by Django 3.1.6 on 2021-02-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210204_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.CharField(choices=[('1', 'user1'), ('2', 'user2'), ('3', 'user3')], default='1', max_length=1),
        ),
    ]