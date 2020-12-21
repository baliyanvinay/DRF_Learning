from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from wish.models import Wish
from wish.serializers import WishSerializer, UserSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from wish.permissions import IsOwnerOrReadOnly

# Tutorial 5: HyperLinking and root api defination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'wishes': reverse('wish-list', request=request, format=format)
    })


# Tutorial 1: Serialization


@csrf_exempt
def wish_list(request):
    """
    List all wishes or create a new wish
    """
    if request.method == 'GET':
        all_wishes = Wish.objects.all()
        wish_serializer = WishSerializer(all_wishes, many=True)  # serialized
        return JsonResponse(wish_serializer.data, safe=False)

    if request.method == 'POST':
        # Write method Implementation here
        parsed_data = JSONParser.parse(request)
        serialized_data = WishSerializer(data=parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def wish_detail(request, pk):
    """
    Retrieve, update or delete a birthday wish.
    """
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Write method Implementation here
        serialized_wish = WishSerializer(wish)
        return JsonResponse(serialized_wish.data)

    elif request.method == 'PUT':
        # Write method Implementation here
        parsed_data = JSONParser.parse(request)
        serialized_data = WishSerializer(data=parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data)
        else:
            return JsonResponse(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Write method Implementation here
        wish.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Tutorial 3: Class Based Views Tutorial 4: Authentications and Permissions
# Class Based Views :: Handles basically all the operations that we did using function based views
# WishList for Listing and Creating data | RetrieveUpdateDestroy is for handling single object


class WishList(generics.ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    # Authenticated  user can edit| All can read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        # POST request can only be made when owner of wish serializer matches request.user
        serializer.save(owner=self.request.user)


class WishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    # Permissions: Owner can update, destroy
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
