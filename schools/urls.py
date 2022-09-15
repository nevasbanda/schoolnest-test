from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowAllSchools, name='showSchools'),
    path('db_school/', views.SchoolData, name='db_school'),
    path('school/<int:pk>/', views.SchoolDetail, name='schoolDetail'),
    path('addSchool/', views.addSchool, name='addSchool'),
    path('updateSchool/<int:pk>/', views.updateSchool, name='updateSchool'),
    path('deleteSchool/<int:pk>/', views.deleteSchool, name='deleteSchool'),
    path('search/', views.searchBar, name='search'),
]

