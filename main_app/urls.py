from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('weavers/', views.weavers_index, name='index'),
    path('weavers/<int:weaver_id>/', views.weavers_detail, name='detail'),
    path('weavers/create/', views.WeaverCreate.as_view(), name='weavers_create'),
    path('weavers/<int:pk>/update/', views.WeaverUpdate.as_view(), name='weavers_update'),
    path('weavers/<int:pk>/delete/', views.WeaverDelete.as_view(), name='weavers_delete'),
    path('weavers/<int:weaver_id>/add_sighting/', views.add_sighting, name='add_sighting'),
]