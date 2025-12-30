from django.urls import path,include
import views

urlpatterns = [
    path('',views.view_message,name='view_message'),

]