# Generated by Django 4.0.4 on 2022-04-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_currency_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_noob',
            field=models.BooleanField(default=True),
        ),
    ]