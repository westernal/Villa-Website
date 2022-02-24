from django.urls import path
from quickstart.views import getAllData, updateVilla, createVilla

urlpatterns = [
     path('data/', getAllData.as_view()),
     path('data/update/<int:primaryKey>/', updateVilla.as_view()),
     path('data/create/', createVilla.as_view()),
]
