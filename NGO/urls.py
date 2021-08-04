from django.urls import path
from . import views


urlpatterns = [
    
    path('list/', views.RequestListView.as_view(), name='lists'),
    path('create/', views.RequestCreateView.as_view(), name='create-request'),
    #path('request/<int:pk>', views.RequestDetailView.as_view(), name='request-detail'),

    path('create-cat', views.CategoryCreateView.as_view(), name='create-cat'),
    path('detail/<int:pk>/', views.RequestDetailView.as_view(), name='detail'),
]
