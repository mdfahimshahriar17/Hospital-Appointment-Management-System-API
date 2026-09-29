from django.urls import path
from . import views

urlpatterns = [
    path('', views.BillingListCreateView.as_view(), name='billing-list-create'),
    path('<int:pk>/', views.BillingDetailView.as_view(), name='billing-detail'),
]