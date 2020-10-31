from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tank-index'),
    path('users/tank/create', views.tankcreation, name='tank-create'),
    path('users/tank/fertilizer/tank', views.fertilizercreation, name='fertilizer-create'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/', views.SignUpView.as_view(), name='signup'),
    path('users/tank/', views.tanklist, name='tank-list'),
    path('users/tank/<int:id>/update/', views.updatetank, name='tank-update'),
    path('users/tank/<int:id>/delete/', views.deletetank, name='delete-tank'),
]
