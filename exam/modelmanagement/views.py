from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Restaurant, Dish
from .serializers import RestaurantSerializer, DishSerializer


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
        serializer = BookSerializer(instance)
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
        books = Dish.objects.all()
        serializer = DishSerializer(books, many=True)
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