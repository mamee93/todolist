from django.urls import path
from  .views import list,delete_list,update_list



urlpatterns = [
    path('',list,name='list'),
    path('update_list/<str:pk>/',update_list, name='update_list'),
    path('delete/<int:id>/',delete_list, name='delete_list'),


]