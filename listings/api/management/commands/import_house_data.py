import csv
import re

from datetime import datetime
from django.core.management.base import BaseCommand, CommandError

from api.models import House, ZillowListing


class Command(BaseCommand):
    help = 'Imports data about houses'

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            dest="csv",
            default="",
            help=("CSV file to import house data from")
        )

    def handle(self, *args, **options):
        csv_file_name = options.get("csv", None)

        if not csv_file_name:
            raise CommandError(
                "No CSV file specified! use --csv <csv_file_name> to specify a CSV file."
            )

        self.parse_csv_file(csv_file_name)

    def parse_csv_file(self, csv_file_name):
        with open(csv_file_name, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
            zillow_listings = []

            for row in csv_reader:
                for key, val in row.items():
                    if not val:
                        row[key] = None

                house = House.objects.create(
                    area_unit=row["area_unit"],
                    bathrooms=row["bathrooms"],
                    bedrooms=row["bedrooms"],
                    home_size=row["home_size"],
                    home_type=row["home_type"],
                    property_size=row["property_size"],
                    address=row["address"],
                    city=row["city"],
                    state=row["state"],
                    zipcode=row["zipcode"],
                    year_built=row["year_built"]
                )

                zillow_listings.append(ZillowListing(
                    id=int(row["zillow_id"]),
                    estimate_amount=row["zestimate_amount"],
                    estimate_last_updated=self.normalize_date(
                        row["zestimate_last_updated"]
                    ),
                    house=house,
                    last_sold_date=self.normalize_date(
                        row["last_sold_date"]
                    ),
                    last_sold_price=row["last_sold_price"],
                    link=row["link"],
                    price=self.normalize_price(row["price"]),
                    rent_price=row["rent_price"],
                    rent_estimate_amount=row["rentzestimate_amount"],
                    rent_estimate_last_updated=self.normalize_date(
                        row["rentzestimate_last_updated"]
                    ),
                    tax_value=row["tax_value"],
                    tax_year=row["tax_year"]
                ))

        ZillowListing.objects.bulk_create(zillow_listings)

    def normalize_price(self, price):
        if not price:
            return None

        numeral = float(re.findall(r'\d+\.?\d*', price)[0])
        multiplier_value = price[-1]

        if multiplier_value == 'M':
            return numeral * 1000000

        if multiplier_value == 'K':
            return numeral * 1000

        return None

    def normalize_date(self, date):
        if not date:
            return None

        return datetime.strptime(
            date, '%M/%d/%Y'
        )
