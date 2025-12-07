from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import restaurant
from .serializers import RestaurantSerializer


@api_view(['GET'])
def getData(request):
    restaurants = restaurant.objects.all()
    if not restaurants:
        return Response({'error':'no data'}, status=status.HTTP_404_NOT_FOUND)
    serialized = RestaurantSerializer(restaurants, many=True)
    return Response(serialized.data)



@api_view(['POST'])
def insertData(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delData(request, id):
    try:
        aimed = restaurant.objects.get(id_restaurant=id)
    except restaurant.DoesNotExist:
        return Response({'error': 'restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

    aimed.delete()
    return Response({'message': 'restaurant deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT'])
def updateData(request):
    id = request.data.get("id_restaurant")
    try:
        restaurant_obj = restaurant.objects.get(id_restaurant=id)
    except restaurant.DoesNotExist:
        return Response({'error': 'restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RestaurantSerializer(restaurant_obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
