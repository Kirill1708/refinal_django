from django.urls import path

from .views import DishViewSet, DishListView, RestaurantListView, RestaurantViewSet

urlpatterns = [
    path('dishes/', DishListView.as_view()),
    path('dishes/create/', DishViewSet.as_view({'post': 'create'})),
    path('dishes/<int:pk>/', DishViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'})),
    path('restaurants/', RestaurantListView.as_view()),
    path('restaurants/create/', RestaurantViewSet.as_view({'post': 'create'})),
    path('restaurants/<int:pk>/', RestaurantViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'})),
    
]