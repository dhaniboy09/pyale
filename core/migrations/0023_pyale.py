# Generated by Django 2.1.4 on 2019-01-27 12:20

import cloudinary.models
from decimal import Decimal
import dirtyfields.dirtyfields
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_pyale'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', cloudinary.models.CloudinaryField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PropertyRunningCosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_description', models.TextField()),
                ('amount_spent_currency', djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3)),
                ('amount_spent', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=19)),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='property',
            name='total_cost_currency',
        ),
        migrations.AddField(
            model_name='property',
            name='current_rental_value',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Rental Value of Property in Naira for current year', max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='current_rental_value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='property',
            name='net_revenue',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Net Revenue of Property in Naira for current year', max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='net_revenue_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='property',
            name='property_value',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Value of Property in Naira', max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='property',
            name='rental_revenue',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, help_text='Payable Revenue on property in Naira for current year', max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='rental_revenue_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('NGN', 'Naira')], default='NGN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='property',
            name='year',
            field=models.CharField(default=2019, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='letting',
            name='deposit',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), help_text='Deposit for this letting (in Naira)', max_digits=19),
        ),
        migrations.AlterField(
            model_name='letting',
            name='service_charge',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), help_text='Annual Service Charge (in Naira)', max_digits=19),
        ),
        migrations.AlterField(
            model_name='letting',
            name='total_letting_cost',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), help_text='Total Cost for the letting period (in Naira)', max_digits=19),
        ),
        migrations.AlterField(
            model_name='paymentschedule',
            name='amount_due',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), help_text='The amount to be paid per cycle e.g. the amount per month or per quarter (in Naira)', max_digits=19),
        ),
        migrations.AddField(
            model_name='propertyrunningcosts',
            name='realty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property'),
        ),
        migrations.AddField(
            model_name='propertydocument',
            name='realty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Property'),
        ),
    ]
