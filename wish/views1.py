from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from wishes.models import Wish
from wishes.serializers import WishSerializer

# Tutorial 2: Requests and Responses


@api_view(['GET', 'POST'])
def wish_list(request, format=None):
    """
    List all wishes or create a new wish
    """
    # GET method implementation here
    if request.method == 'GET':
        all_wishes = Wish.objects.all()
        wish_serializer = WishSerializer(all_wishes, many=True)  # serialized
        return Response(wish_serializer.data)

    # POST method implementation here
    if request.method == 'POST':
        # Write method Implementation here

        serialized_data = WishSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def wish_detail(request, pk, format=None):
    """
    Retrieve, update or delete a birthday wish.
    """
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET method implementation here
    if request.method == 'GET':
        # Write method Implementation here
        serialized_wish = WishSerializer(wish)
        return Response(serialized_wish.data)

    # PUT method implementation here
    elif request.method == 'PUT':
        # Write method Implementation here
        serialized_data = WishSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method implementation here
    elif request.method == 'DELETE':
        # Write method Implementation here
        wish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
