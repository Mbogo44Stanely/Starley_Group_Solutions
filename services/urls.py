from django.urls import path

from .views import service_list, service_detail


urlpatterns = [
    path('', service_list, name='services'),
    path('<slug:slug>/', service_detail, name='service-detail'),
]
