from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='dash'),
    path('category/', views.view_category, name='category'),
    path('category/<category_id>', views.view_category, name='category'),
    path('show_book/', views.pdf_view, name='show_book'),
    path('show_book/<ebook_id>', views.pdf_view, name='show_book'),
]
