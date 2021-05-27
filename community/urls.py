from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('titles/', views.movie_title),
    path('review/', views.review_list),
    path('review/<int:review_id>/detail/', views.review_detail),
    path('review/<int:review_id>/review_like/', views.review_like),
    path('review/<int:review_id>/comment/', views.comment_list),
    path('review/<int:review_id>/comment/<int:comment_id>/detail/', views.comment_detail),
    path('review/search/', views.review_search)    
]