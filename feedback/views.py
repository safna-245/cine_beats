from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from filim.models import Movie

from feedback.serializers import ReviewSerializer
from feedback.models import Review
from feedback.permissions import IsOwner

# Create your views here.
class ReviewCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_id = pk

        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data

        serializer_instance = ReviewSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object,owner=request.user)

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

class ReviewRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = ReviewSerializer

    queryset = Review.objects.all()

    
            