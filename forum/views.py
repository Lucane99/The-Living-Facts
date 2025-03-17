from rest_framework import viewsets
from .serializers import DiscussionSerializer, CommentSerializer
from .models import Discussion, Comment

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
