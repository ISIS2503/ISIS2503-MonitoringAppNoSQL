from django.urls import path
from .views import places, placeDetail, measurements, average

urlpatterns = [
    path('places/', places),
    path('places/<place_id>/', placeDetail),
    path('places/<place_id>/measurements/', measurements),
    path('measurements/<place_id>/', measurements),
    path('average/<place_id>/', average)
]