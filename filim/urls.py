from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from filim.views import SignUpView
from filim.views import MovieListCreateView,MovieRetrieveUpdateDeleteView


urlpatterns=[
    path("signup/",SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("movie/",MovieListCreateView.as_view()),
    path("movie/<int:pk>/",MovieRetrieveUpdateDeleteView.as_view()),
]