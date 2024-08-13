from django.urls import path, include
from . import views

urlpatterns = [
    path('all_chai/', views.home_all_chai, name='all_chai'),
    path('all_chai/<int:chai_id>', views.chai_detail, name='chai_detail'),
    path('all_chai/chai_store', views.chai_stores, name='chai_stores'),
    
]
