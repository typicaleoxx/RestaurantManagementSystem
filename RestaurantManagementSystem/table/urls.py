from .views import TableViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router=DefaultRouter()
router.register(r'table',TableViewSet)

urlpatterns = [
    path('',include(router.urls))
]
