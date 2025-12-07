from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import restaurant
from .serializers import RestaurantSerializer

@api_view(['GET'])
def getData(request):
    restaurants = restaurant.objects.all()
    serialized = RestaurantSerializer(restaurants, many=True)
    return Response(serialized.data)