from django.urls import path,include
from . import views


urlpatterns = [
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/logout/', include('rest_auth.urls')),
    path('delete/', views.account_delete),
    path('profile/', views.profile),
    path('<str:username>/review/', views.user_review),
    path('<str:username>/', views.user_profile),   
    path('<str:username>/update/', views.profile_update),
    path('follow/<str:username>/', views.follow),    
]