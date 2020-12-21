from rest_framework import serializers
from wish.models import Wish
from django.contrib.auth.models import User


class WishSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wish
        fields = ('url', 'id', 'title', 'wishtext', 'owner')


class UserSerializer(serializers.ModelSerializer):
    # All Wished related to a user mapped here
    # wishes = serializers.PrimaryKeyRelatedField(many=True, queryset=Wish.objects.all())
    wishes = serializers.HyperlinkedRelatedField(
        many=True, view_name='wish-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'wishes']
