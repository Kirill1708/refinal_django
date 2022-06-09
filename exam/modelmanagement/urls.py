from django.urls import path
from .views import DishViewSet, DishListView, RestaurantListView, RestaurantViewSet, ReviewListView, ReviewViewSet, RestaurantReviewListView, RestaurantReviewViewSet, DishReviewListView, DishReviewViewSet

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
    path('reviews/', ReviewListView.as_view()),
    path('reviews/create/', ReviewViewSet.as_view({'post': 'create'})),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'})),
    path('restaurant_reviews/', RestaurantReviewListView.as_view()),
    path('restaurant_reviews/create/', RestaurantReviewViewSet.as_view({'post': 'create'})),
    path('restaurant_reviews/<int:pk>/', RestaurantReviewViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'})),
    path('dish_reviews/', DishReviewListView.as_view()),
    path('dish_reviews/create/', DishReviewViewSet.as_view({'post': 'create'})),
    path('dish_reviews/<int:pk>/', DishReviewViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'})),
    
]
