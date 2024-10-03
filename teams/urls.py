from django.urls import path
from .views import PersonListCreateView, PersonDetailView, TeamListCreateView, TeamDetailView

urlpatterns = [
    path('people/', PersonListCreateView.as_view(), name='person-list'),
    path('people/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('teams/', TeamListCreateView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]