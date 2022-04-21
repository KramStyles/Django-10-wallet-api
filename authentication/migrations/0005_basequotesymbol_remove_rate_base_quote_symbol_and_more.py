# Generated by Django 4.0.4 on 2022-04-19 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rate_base_quote_symbol'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseQuoteSymbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pair', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='rate',
            name='base_quote_symbol',
        ),
        migrations.AddField(
            model_name='rate',
            name='base_quote_symbol_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.basequotesymbol'),
            preserve_default=False,
        ),
    ]
