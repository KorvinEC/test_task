from django.urls import path
from api import views


urlpatterns = [
    path('dealers/', views.DealerList.as_view()),
    path('dealers/<int:pk>', views.DealerDetail.as_view()),
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>', views.CarDetail.as_view()),
]
