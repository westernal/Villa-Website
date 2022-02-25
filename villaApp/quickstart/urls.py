from django.urls import path
from quickstart.views import getAllData, updateVilla, createVilla, searchVilla, deleteVilla

urlpatterns = [
     path('data/', getAllData.as_view()),
     path('data/update/<int:id>/', updateVilla.as_view()),
     path('data/create/', createVilla.as_view()),
     path('data/search/', searchVilla.as_view()),
     path('data/delete/<int:id>/', deleteVilla.as_view()),
]
