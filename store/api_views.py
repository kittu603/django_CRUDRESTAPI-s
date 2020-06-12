#views for our API's
from .models import Product
from rest_framework.generics import ListAPIView, CreateAPIView , DestroyAPIView , RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

#how many items to show on a page
class ProductsPagination(LimitOffsetPagination):
    default_limit = 2 #how many id's to show by default
    max_limit = 10

#create a form interface for adding new data to api
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer #which serialized data to show
    #post submit, a new id will be appended to already present data


#READ,UPDATE and DELETE a particular API view, 
# below can be used instead of DestroyView and UpdateView and also for getting specific view
class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # what to show in List view
    lookup_field = 'id'  #which specific id in data, passed to urls to regex
    serializer_class = ProductSerializer #which serialized data to show

# like R in CRUD, getting and showing the API data
class ProductListApiView(ListAPIView):
    queryset = Product.objects.all() #what to show in List view
    serializer_class = ProductSerializer #which serialized data to show
    filter_backends = (DjangoFilterBackend,SearchFilter) #which filter setting to work
    filter_fields = ('name', 'id') #fields needing filter
    search_fields = ('name', 'id') #fields needing search
    pagination_class = ProductsPagination #which pagination class to use

# class ProductDeleteview(DestroyAPIView):
#     queryset = Product.objects.all()
#     lookup_field = ('id',) #delete by which field








