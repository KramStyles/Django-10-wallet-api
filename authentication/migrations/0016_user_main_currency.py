# Generated by Django 4.0.4 on 2022-04-23 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_merge_20220422_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='main_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.currency'),
        ),
    ]
