from rest_framework import mixins, viewsets, pagination

from api.models import House, ZillowListing
from api.serializers import HouseSerializer, ZillowListingSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000


class HouseViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['city', 'zipcode', 'bedrooms', 'bathrooms']


class ZillowListingViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
):
    queryset = ZillowListing.objects.all()
    serializer_class = ZillowListingSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = [
        'house',
        'house__city',
        'house__zipcode',
        'house__bedrooms',
        'house__bathrooms'
    ]
