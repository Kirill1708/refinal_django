from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from .serializers import RestaurantSerializer, DishSerializer, ReviewSerializer, RestaurantReviewSerializer, DishReviewSerializer


class RestaurantListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class RestaurantViewSet(ViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Restaurant.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = Restaurant.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DishListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)


class DishViewSet(ViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = Dish.objects.get(id=pk)
        serializer = DishSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Dish.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = Dish.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReviewListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(ViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = Review.objects.get(id=pk)
        serializer = ReviewSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Review.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = Review.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RestaurantReviewListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = RestaurantReview.objects.all()
        serializer = RestaurantReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class RestaurantReviewViewSet(ViewSet):
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = RestaurantReview.objects.get(id=pk)
        serializer = RestaurantReviewSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = RestaurantReview.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = RestaurantReview.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DishReviewListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = DishReview.objects.all()
        serializer = DishReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class DishReviewViewSet(ViewSet):
    queryset = DishReview.objects.all()
    serializer_class = DishReviewSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        instance = DishReview.objects.get(id=pk)
        serializer = DishReviewSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = DishReview.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        instance = DishReview.objects.get(id=pk)
        try:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)