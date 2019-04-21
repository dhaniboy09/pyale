# Generated by Django 2.1.4 on 2019-04-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_pyale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bank',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='billing_cycle',
            field=models.CharField(blank=True, help_text='Automatically Populated for Service Charge. Might not be required for other bills', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='card_brand',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='card_expiry_month',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='card_expiry_year',
            field=models.CharField(blank=True, editable=False, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='card_type',
            field=models.CharField(blank=True, editable=False, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='is_mobile',
            field=models.BooleanField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='last4',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='name',
            field=models.CharField(help_text='A title for this bill', max_length=255),
        ),
        migrations.AlterField(
            model_name='bills',
            name='transaction_date',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='transaction_id',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='transaction_reference',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='transaction_time',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='letting',
            name='deposit_refunded',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('employed', 'Employed'), ('unemployed', 'Unemployed'), ('self_employed', 'Self Employed')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('ms', 'Ms'), ('dr', 'Dr')], max_length=50, null=True),
        ),
    ]