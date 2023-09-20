from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lead/<int:lead_id>/', views.lead_detail, name='lead_detail'),
path('lead/<int:lead_id>/add_activity/', views.add_activity, name='add_activity'),

]
