from django.urls import path, include
from wish import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# Created a router and register our viewsets with it.
router = DefaultRouter()
router.register('wishes', views.WishViewSet)
router.register('users', views.UserViewSet)

# path('', include(router.urls)), # add this to get urls for all viewsets
urlpatterns = [
    path('', include(router.urls)),
]

# # Wishes related paths
# urlpatterns = [
#     path('wishes/', views.WishList.as_view(), name="wish-list"),
#     path('wishes/<int:pk>', views.WishDetail.as_view(), name="wish-detail"),
# ]

# # User related paths
# urlpatterns += [
#     path('users/', views.UserList.as_view(), name="user-list"),
#     path('users/<int:pk>', views.UserDetail.as_view(), name="user-detail"),
# ]

# # Login and Logout paths
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]

# # Entry endpoint or home path
# urlpatterns += [
#     path('', views.api_root, name='api-root'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
