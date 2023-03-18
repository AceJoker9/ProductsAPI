from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def product_list(request):
    supply = Product.objects.all()
    serializer =  ProductSerializer(supply, many=True)

    return Response(serializer.data)

