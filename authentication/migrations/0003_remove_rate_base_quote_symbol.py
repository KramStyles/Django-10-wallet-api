# Generated by Django 4.0.4 on 2022-04-19 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rate_quote_currency_id_alter_rate_base_currency_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='base_quote_symbol',
        ),
    ]
