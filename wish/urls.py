from django.urls import path
from wish import views

urlpatterns = [
    path('wishes/', views.WishList.as_view()),
    path('wishes/<int:pk>', views.WishDetail.as_view()),
]
