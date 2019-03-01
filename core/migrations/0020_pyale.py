# Generated by Django 2.1.4 on 2019-01-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_pyale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letting',
            name='letting_duration',
            field=models.IntegerField(default=0, help_text='Letting period (must be in years)'),
        ),
        migrations.AlterField(
            model_name='paymentschedule',
            name='amount_due',
            field=models.CharField(editable=False, help_text='The amount to be paid per cycle e.g. the amount per month or per quarter', max_length=512),
        ),
        migrations.AlterField(
            model_name='paymentschedule',
            name='payment_cycle',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='paymentschedule',
            name='tag',
            field=models.CharField(default='Rent', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='tag',
            field=models.CharField(help_text='A unique name for this image', max_length=255, unique=True),
        ),
    ]