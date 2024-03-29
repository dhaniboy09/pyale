# Generated by Django 2.1.4 on 2019-03-17 00:21

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_pyale'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('current_state', models.TextField(max_length=512)),
                ('original_state', models.TextField(max_length=512)),
                ('cost_incurred_currency', djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3)),
                ('cost_incurred', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=19)),
            ],
        ),
    ]
