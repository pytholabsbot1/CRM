from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lead/<int:lead_id>/', views.lead_detail, name='lead_detail'),
   path('add_call_activity/<int:lead_id>/', views.add_call_activity, name='add_call_activity'),
   ]
