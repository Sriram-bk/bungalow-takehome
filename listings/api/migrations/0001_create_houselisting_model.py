# Generated by Django 3.2.8 on 2021-10-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('area_unit', models.CharField(choices=[('SqFt', 'Square Feet')], default='SqFt', max_length=4)),
                ('home_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'Multi-Family 2 To 4'), ('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land')], default='Miscellaneous', max_length=25)),
                ('home_size', models.PositiveIntegerField(blank=True, null=True)),
                ('property_size', models.PositiveIntegerField(blank=True, null=True)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bedrooms', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('year_built', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=8)),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_sold_price', models.PositiveIntegerField(blank=True, null=True)),
                ('link', models.URLField()),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('rent_price', models.PositiveIntegerField(blank=True, null=True)),
                ('rentzestimate_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('rentzestimate_last_updated', models.DateField(blank=True, null=True)),
                ('tax_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('tax_year', models.PositiveIntegerField(blank=True, null=True)),
                ('zestimate_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('zestimate_last_updated', models.DateField(blank=True, null=True)),
                ('zillow_id', models.UUIDField(db_index=True, unique=True)),
            ],
        ),
    ]
