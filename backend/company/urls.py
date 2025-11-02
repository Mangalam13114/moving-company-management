from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quote/', views.quote_form, name='quote_form'),
    path('quote/<int:quote_id>/', views.quote_detail, name='quote_detail'),
    path('quote/<int:quote_id>/update-status/', views.update_quote_status, name='update_quote_status'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/<int:quote_id>/', views.inventory, name='inventory_detail'),
    path('schedule/', views.schedule, name='schedule'),
    path('insurance/', views.insurance, name='insurance'),
    path('insurance/<int:claim_id>/update-status/', views.update_claim_status, name='update_claim_status'),
]
