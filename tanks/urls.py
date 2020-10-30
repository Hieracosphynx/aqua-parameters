from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tank-index'),
    path('create/', views.tankcreation, name='tank-create'),
    path('create/fertilizer', views.fertilizercreation, name='fertilizer-create'),
    path('users/', include('django.contrib.auth.urls')),
]
