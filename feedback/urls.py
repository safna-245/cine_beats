from django.urls import path
from feedback.views import ReviewCreateView,ReviewRetrieveUpdateDeleteView

urlpatterns=[
    path("movie/<int:pk>/review/",ReviewCreateView.as_view()),
    path("<int:pk>/review/",ReviewRetrieveUpdateDeleteView.as_view()),
]