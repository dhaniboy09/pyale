# Generated by Django 2.1.4 on 2019-03-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_pyale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_landlord_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_landlord_mobile_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_landlord_mobile_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employer_contact_person',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employer_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employer_mobile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employer_telephone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='length_of_time_at_last_property',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_house_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='House Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_house_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='House Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_mobile_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_mobile_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_relationship_to_tenant',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Realtionship to Tenant'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='user',
            name='next_of_kin_town',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Town'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_duration_of_stay',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Duration of Stay'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_house_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='House Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_house_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='House Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_address_town',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Town'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referee_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referee_mobile_number_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referee_mobile_number_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referee_relationship_to_tenant',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Relationship to Tenant'),
        ),
        migrations.AlterField(
            model_name='user',
            name='years_at_current_employment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
