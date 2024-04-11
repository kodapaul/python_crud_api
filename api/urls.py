from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

#URL Structure for the API
urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('item/<int:pk>', LocationDetail.as_view()),
]
