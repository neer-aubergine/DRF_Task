from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from blogs.models import Blog

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, blog=blog)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        comments = Comment.objects.filter(blog=blog)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def delete(self, request, comment_id, blog_id):
        blog = get_object_or_404(Blog, id=blog_id, author=request.user)
        comment = get_object_or_404(Comment, id=comment_id, blog=blog)
        comment.delete()
        return Response({"message": "Comment deleted successfully"}, status=204)