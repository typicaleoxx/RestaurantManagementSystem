from rest_framework.routers import DefaultRouter
from .views import BillViewSet, ReservationViewSet
from django.urls import path , include

router=DefaultRouter()
router.register(r'bill',BillViewSet)
router.register(r'reservation',ReservationViewSet)

urlpatterns = [
    path('',include(router.urls))
]