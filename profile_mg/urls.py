from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('share',views.share_profile, name='share_profile'),

]