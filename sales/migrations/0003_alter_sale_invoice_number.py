# Generated by Django 3.2.5 on 2021-12-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20211213_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='invoice_number',
            field=models.CharField(default='9461513087', max_length=10, unique=True),
        ),
    ]