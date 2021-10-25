from django.shortcuts import render

from rest_framework import mixins, viewsets

from api.models import House, ZillowListing
from api.serializers import HouseSerializer, ZillowListingSerializer


class HouseViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ZillowListingViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
):
    queryset = ZillowListing.objects.all()
    serializer_class = ZillowListingSerializer
