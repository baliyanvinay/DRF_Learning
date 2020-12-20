from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from wish.models import Wish
from wish.serializers import WishSerializer


@csrf_exempt
def wish_list(request):
    all_wishes = Wish.objects.all()
    """
    List all wishes or create a new wish
    """
    if request.method == 'GET':
        # Write method Implementation here
        wish_serializer = WishSerializer(all_wishes)  # serialized
        return JsonResponse(wish_serializer.data)

    if request.method == 'POST':
        # Write method Implementation here
        parsed_data = JSONParser(request.data)
        serialized_data = WishSerializer(parsed_data)
        if serialized_data.is_valid():
            return JsonResponse(serialized_data.validated_data)
        else:
            return JsonResponse(serialized_data.errors)


@csrf_exempt
def wish_detail(request, pk):
    """
    Retrieve, update or delete a birthday wish.
    """
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # Write method Implementation here
        serialized_wish = WishSerializer(wish)
        return JsonResponse(serialized_wish.data)

    elif request.method == 'PUT':
        # Write method Implementation here
        parsed_data = JSONParser(request.data)
        serialized_data = WishSerializer(parsed_data)
        if serialized_data.is_valid():
            return JsonResponse(serialized_data.validated_data)
        else:
            return JsonResponse(serialized_data.errors)

    elif request.method == 'DELETE':
        # Write method Implementation here
        wish.delete()
        return HttpResponse(status_code=204)
