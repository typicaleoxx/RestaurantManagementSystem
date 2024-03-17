from .views import WaiterViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'waiter',WaiterViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
