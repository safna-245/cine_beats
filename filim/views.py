from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from filim.serializers import UserSerializer,MovieSerializer
from filim.models import Movie
from filim.permissions import IsOwner



class SignUpView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)



class MovieListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        instance = Movie.objects.all()

        serializer_instance = MovieSerializer(instance, many=True)

        return Response(data=serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = MovieSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(created_by=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class MovieRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = MovieSerializer

    queryset = Movie.objects.all()