from django.contrib.auth.models import User

from rest_framework import serializers

from filim.models import Movie

from music.models import Song
from music.serializers import SongSerializer

from feedback.models import Review
from feedback.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):

    song_count = serializers.SerializerMethodField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    review = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at","created_by"]

    def get_song_count(self,obj):

        return Song.objects.filter(moviename=obj).count()

    def get_songs(self,obj):

        song_object = Song.objects.filter(moviename=obj)

        serializer_instance = SongSerializer(song_object,many=True)

        return serializer_instance.data

    def get_review(self,obj):

        review_object = Review.objects.filter(movie=obj)

        serializer_instance = ReviewSerializer(review_object,many=True)

        return serializer_instance.data

    
class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ["username","email","password"]
        read_only_fields = ["id"]