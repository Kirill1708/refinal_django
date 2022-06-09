from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField("Name", max_length=50)
    telephone = models.CharField('Telephone', max_length=12)
    city = models.CharField("City", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Dish(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True, editable=True)

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)