from rest_framework import serializers
from .models import Discussion, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'discussion', 'text', 'created_at']

class DiscussionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Discussion
        fields = ['id', 'data', 'title', 'description', 'created_at', 'comments']
