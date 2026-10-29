from rest_framework import serializers

from music.models import Song

class SongSerializer(serializers.ModelSerializer):

    class Meta:

        model = Song

        fields = "__all__"

        read_only_fields = ["id","moviename","created_at","updated_at","created_by"]