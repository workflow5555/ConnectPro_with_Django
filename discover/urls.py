from django.urls import path

import views


urlpatterns = [
    path('',views.view_discover,name='view_discover'),
]