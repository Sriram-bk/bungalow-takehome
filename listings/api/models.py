from django.db import models


class House(models.Model):
    AREA_UNIT_CHOICES = [("SqFt", "Square Feet")]
    HOME_TYPE_CHOICES = [
        ("Apartment", "Apartment"),
        ("Condominium", "Condominium"),
        ("Duplex", "Duplex"),
        ("Miscellaneous", "Miscellaneous"),
        ("MultiFamily2To4", "Multi-Family 2 To 4"),
        ("SingleFamily", "Single Family"),
        ("VacantResidentialLand", "Vacant Residential Land"),
    ]

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    area_unit = models.CharField(
        choices=AREA_UNIT_CHOICES,
        max_length=4,
        default="SqFt"
    )
    home_type = models.CharField(
        choices=HOME_TYPE_CHOICES,
        max_length=25,
        default="Miscellaneous"
    )
    home_size = models.PositiveIntegerField(null=True, blank=True)
    property_size = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    bedrooms = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    year_built = models.IntegerField(null=True, blank=True)

    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=8)


class ZillowListing(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    id = models.BigIntegerField(
        primary_key=True,
        editable=False
    )
    estimate_amount = models.PositiveIntegerField(null=True, blank=True)
    estimate_last_updated = models.DateField(null=True, blank=True)
    house = models.ForeignKey(
        House,
        related_name='zillow_listing',
        on_delete=models.CASCADE
    )
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.PositiveIntegerField(null=True, blank=True)
    link = models.URLField()
    price = models.PositiveIntegerField(null=True, blank=True)
    rent_price = models.PositiveIntegerField(null=True, blank=True)
    rent_estimate_amount = models.PositiveIntegerField(null=True, blank=True)
    rent_estimate_last_updated = models.DateField(null=True, blank=True)
    tax_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True
    )
    tax_year = models.PositiveIntegerField(null=True, blank=True)
