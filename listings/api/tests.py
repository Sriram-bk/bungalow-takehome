from django.test import TestCase
from django.http import HttpRequest
from rest_framework.request import Request
from model_bakery import baker

from api.models import House, ZillowListing
from api.views import HouseViewSet, ZillowListingViewSet
from api.serializers import HouseSerializer, ZillowListingSerializer


class HouseTestCase(TestCase):
    def setUp(self):
        prepared_request = Request(request=HttpRequest())
        self.prepared_house_viewset = HouseViewSet(
            request=prepared_request,
            format_kwarg={}
        )
        self.prepared_house = baker.prepare(House)

    def get_serialized_data(self):
        return {
            "id": self.prepared_house.id,
            "area_unit": self.prepared_house.area_unit,
            "home_type": self.prepared_house.home_type,
            "home_size": self.prepared_house.home_size,
            "property_size": self.prepared_house.property_size,
            "bathrooms": self.prepared_house.bathrooms,
            "bedrooms": self.prepared_house.bedrooms,
            "year_built": self.prepared_house.year_built,
            "address": self.prepared_house.address,
            "city": self.prepared_house.city,
            "state": self.prepared_house.state,
            "zipcode": self.prepared_house.zipcode
        }

    def test_viewset_serializer(self):
        serializer = self.prepared_house_viewset.get_serializer()
        self.assertIsInstance(serializer, HouseSerializer)

    def test_viewset_filter_fields(self):
        filterset_fields = ['city', 'zipcode', 'bedrooms', 'bathrooms']
        self.assertEqual(filterset_fields, HouseViewSet.filterset_fields)

    def test_serializer_setup_with_expected_fields(self):
        expected_fields = (
            "id",
            "area_unit",
            "home_type",
            "home_size",
            "property_size",
            "bathrooms",
            "bedrooms",
            "year_built",
            "address",
            "city",
            "state",
            "zipcode"
        )

        self.assertEqual(expected_fields, HouseSerializer.Meta.fields)

    def test_serializer_serialization(self):
        expected_serialized_data = self.get_serialized_data()
        serializer = HouseSerializer(self.prepared_house)

        self.assertDictEqual(serializer.data, expected_serialized_data)


class ZillowListingTestCase(TestCase):
    def setUp(self):
        prepared_request = Request(request=HttpRequest())
        self.prepared_zillow_listing_viewset = ZillowListingViewSet(
            request=prepared_request,
            format_kwarg={}
        )
        self.prepared_zillow_listing = baker.prepare(ZillowListing)

    def get_serialized_data(self):
        return {
            "id": self.prepared_zillow_listing.id,
            "house": {
                "id": self.prepared_zillow_listing.house.id,
                "area_unit": self.prepared_zillow_listing.house.area_unit,
                "home_type": self.prepared_zillow_listing.house.home_type,
                "home_size": self.prepared_zillow_listing.house.home_size,
                "property_size": self.prepared_zillow_listing.house.property_size,
                "bathrooms": self.prepared_zillow_listing.house.bathrooms,
                "bedrooms": self.prepared_zillow_listing.house.bedrooms,
                "year_built": self.prepared_zillow_listing.house.year_built,
                "address": self.prepared_zillow_listing.house.address,
                "city": self.prepared_zillow_listing.house.city,
                "state": self.prepared_zillow_listing.house.state,
                "zipcode": self.prepared_zillow_listing.house.zipcode
            },
            "created": self.prepared_zillow_listing.created,
            "updated": self.prepared_zillow_listing.updated,
            "estimate_amount": self.prepared_zillow_listing.estimate_amount,
            "estimate_last_updated": self.prepared_zillow_listing.estimate_last_updated,
            "last_sold_date": self.prepared_zillow_listing.last_sold_date,
            "last_sold_price": self.prepared_zillow_listing.last_sold_price,
            "link": self.prepared_zillow_listing.link,
            "price": self.prepared_zillow_listing.price,
            "rent_price": self.prepared_zillow_listing.rent_price,
            "rent_estimate_amount": self.prepared_zillow_listing.rent_estimate_amount,
            "rent_estimate_last_updated": self.prepared_zillow_listing.rent_estimate_last_updated,
            "tax_value": self.prepared_zillow_listing.tax_value,
            "tax_year": self.prepared_zillow_listing.tax_year
        }

    def test_viewset_serializer(self):
        serializer = self.prepared_zillow_listing_viewset.get_serializer()
        self.assertIsInstance(serializer, ZillowListingSerializer)

    def test_viewset_filter_fields(self):
        filterset_fields = [
            'house',
            'house__city',
            'house__zipcode',
            'house__bedrooms',
            'house__bathrooms'
        ]
        self.assertEqual(
            filterset_fields,
            ZillowListingViewSet.filterset_fields
        )

    def test_serializer_setup_with_expected_fields(self):
        expected_fields = '__all__'
        self.assertEqual(expected_fields, ZillowListingSerializer.Meta.fields)

    def test_serializer_serialization(self):
        expected_serialized_data = self.get_serialized_data()
        serializer = ZillowListingSerializer(self.prepared_zillow_listing)

        self.assertDictEqual(serializer.data, expected_serialized_data)
