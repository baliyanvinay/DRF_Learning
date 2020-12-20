from django.urls import path
from wish import views

urlpatterns = [
    path('wishes/', views.wish_list),
    path('wishes/<int:pk>', views.wish_detail),
]
