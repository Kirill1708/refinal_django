from rest_framework.serializers import ModelSerializer

from .models import Restaurant, Dish, Review, RestaurantReview, DishReview


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class RestaurantReviewSerializer(ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = "__all__"

class DishReviewSerializer(ModelSerializer):
    class Meta:
        model = DishReview
        fields = "__all__"