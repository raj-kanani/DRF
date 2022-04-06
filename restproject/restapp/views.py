from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, generics
from rest_framework import status
from rest_framework.decorators import api_view


#  1) CRUD operation with api_view decorator.

# create items with post data.
@api_view(['POST'])
def AddApi(request):
    item = ItemSerializer(data=request.data)

    # validate for existing data..
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('this data already exist..')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ShowApi(request):
    # check parameter in url.
    if request.query_params:
        # if you use query_param replacing request.get
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#  update data
@api_view(['POST'])
def UpdateApi(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# delete data
@api_view(['DELETE'])
def DeleteApi(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


# throttle classes
# class One(UserRateThrottle):
#     rate = '1/day'
#
# @api_view(['GET'])
# @throttle_classes(One)
# def view(request):
#     return Response({'message': 'hello this is throttle'})


# class CustomAutoSchema(AutoSchema):
#     def get_link(self, path, method, base_url):
#         pass
#
# @api_view(['GET'])
# @schema(CustomAutoSchema())
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})


#  2)  Generic class based CRUD Operation.........

class AddApi2(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ShowApi2(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UpdateApi2(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DeleteApi2(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


#  CRUD using mixin class............
# create
class AddApi3(GenericAPIView, CreateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # generate create auto form and post
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# list
class ShowApi3(GenericAPIView, ListModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# retrieve
class RetrieveApi3(GenericAPIView, RetrieveModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)


# update
class UpdateApi3(GenericAPIView, UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def post(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)


# destroy
class DeleteApi3(GenericAPIView, DestroyModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


# concreate view classes....

class ListCreateApi(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_fields = ['name', 'amount']


class GetputdeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# # create queryset..
# item = Item.objects.all()
# # convert queryset into python dict / serializing queryset
# all_item = ItemSerializer(item, many=True)
