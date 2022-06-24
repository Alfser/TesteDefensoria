from django.urls import path

from peopleform import views

app_name = 'peopleform' #namespace do app ajudrá a conectar o nome das das rotas as urls.

urlpatterns = [
    path('', views.PersonList.as_view(), name='list'),
    path('create/', views.PersonCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.PersonUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.PersonDetails.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PersonDelete.as_view(), name='delete'),
]