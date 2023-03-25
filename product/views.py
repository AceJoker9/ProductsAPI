from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET', 'POST'])
def product_list(request):


    if request.method == 'GET':
        supply = Product.objects.all()
        serializer =  ProductSerializer(supply, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
           
       
        


