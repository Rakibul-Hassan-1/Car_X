from django.urls import path,include
from . import views

urlpatterns = [
  
   
    path('details/<int:id>',views.DetailClassView.as_view(),name="car_details"),
    

]