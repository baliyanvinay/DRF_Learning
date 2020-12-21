from django.urls import path, include
from wish import views
from rest_framework.urlpatterns import format_suffix_patterns

# Wishes related paths
urlpatterns = [
    path('wishes/', views.WishList.as_view()),
    path('wishes/<int:pk>', views.WishDetail.as_view()),
]

# User related paths
urlpatterns += [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

# Login and Logout paths
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
