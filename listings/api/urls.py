from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import HouseViewSet, ZillowListingViewSet

# TODO: Create your routers and urls here
router = SimpleRouter()
router.register(r'houses', HouseViewSet, basename='house')
router.register(r'zillow-listings', ZillowListingViewSet,
                basename='zillow-listing')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
