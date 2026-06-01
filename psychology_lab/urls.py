from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research, name='research'),
    path('team/', views.team, name='team'),
    path('publications/', views.publications, name='publications'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
    # Dynamic pages — must be last
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
