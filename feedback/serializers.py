from rest_framework import serializers

from feedback.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","movie","owner","created_at","updated_at"]

