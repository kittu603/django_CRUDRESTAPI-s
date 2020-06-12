#views for our API's
from .models import Product
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

#how many 
class ProductsPagination(LimitOffsetPagination):
    default_limit = 2 #how many id's to show by default
    max_limit = 2

class ProductListApiView(ListAPIView):
    queryset = Product.objects.all() #what to show in List view
    serializer_class = ProductSerializer #which serialized data to show
    filter_backends = (DjangoFilterBackend,SearchFilter) #which filter setting to work
    filter_fields = ('name', 'id') #fields needing filter
    search_fields = ('name', 'id') #fields needing search
    pagination_class = ProductsPagination #which pagination class to use






