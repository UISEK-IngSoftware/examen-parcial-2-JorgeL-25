from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieDetailView, MovieListView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
     path('api/', include(router.urls)),
]
