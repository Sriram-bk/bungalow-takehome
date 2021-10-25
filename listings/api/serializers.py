from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import House, ZillowListing


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = (
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


class ZillowListingSerializer(serializers.ModelSerializer):
    house = HouseSerializer()

    class Meta:
        model = ZillowListing
        fields = "__all__"
