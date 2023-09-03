from rest_framework import serializers

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Content:
        return Content.objects.create(**validated_data)

    class Meta:
        model = Content
        fields = ["id", "name", "content", "video_url", "course"]
        read_only_fields = ["course"]
