# Generated by Django 4.0.4 on 2022-04-25 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_merge_20220425_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='main_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.currency'),
        ),
    ]
