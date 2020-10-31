from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tank-index'),
    path('create/tank', views.tankcreation, name='tank-create'),
    path('create/tank/fertilizer', views.fertilizercreation, name='fertilizer-create'),
    path('users/tank/', views.tanklist, name='tank-list'),
    path('users/tank/<int:id>/update/', views.updatetank, name='tank-update'),
    path('users/tank/<int:id>/delete/', views.deletetank, name='delete-tank'),
    path('users/', include('django.contrib.auth.urls')),
]
