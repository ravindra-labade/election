from django.urls import path
from .views import add_candidate, show_candidate, update_candidate, delete_candidate


urlpatterns = [
    path('add/', add_candidate, name='add_url'),
    path('show/', show_candidate, name='show_url'),
    path('update/<int:pk>/', update_candidate, name='update_url'),
    path('delete/<int:pk>/', delete_candidate, name='delete_url'),
]
