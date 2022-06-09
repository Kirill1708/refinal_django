from django.contrib import admin
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview

admin.site.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
admin.site.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
admin.site.register(Review)
class DishAdmin(admin.ModelAdmin):
    list_display = ('rating', 'date')
admin.site.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'review')
admin.site.register(DishReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('dish', 'review')
