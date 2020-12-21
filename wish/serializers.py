from rest_framework import serializers
from wish.models import Wish
from django.contrib.auth.models import User


class WishSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wish
        fields = ('id', 'title', 'wishtext', 'owner')


class UserSerializer(serializers.ModelSerializer):
    # All Wished related to a user mapped here
    wishes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Wish.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'wishes']
