from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('search/', views.PostSearchView.as_view(), name='post_search'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/create/', views.PostCreateView.as_view(), name='post_create'),
    path('dashboard/update/<slug:slug>/', views.PostUpdateView.as_view(), name='post_update'),
    path('dashboard/delete/<slug:slug>/', views.PostDeleteView.as_view(), name='post_delete'),
]   