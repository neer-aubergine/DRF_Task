from django.shortcuts import render, get_object_or_404
from blogs.serializers import BlogSerializer
from blogs.models import Blog, Tags, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from rest_framework.permissions import IsAuthenticated , AllowAny

class BlogDetails(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def post(self, request):
        author = request.user
        serializer = BlogSerializer(data=request.data)
        
        if serializer.is_valid():
            tags = request.data.get('tags', [])
            temp_tags = []
            for tag_name in tags:
                try:
                    tag = Tags.objects.get(id=tag_name)  
                    temp_tags.append(tag)
                except Tags.DoesNotExist:
                    return Response({"error": f"Tag '{tag_name}' does not exist"}, status=400)
            blog = serializer.save(author=author)
            blog.tags.set(temp_tags)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=400)
        
    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk, author=request.user)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        
        if serializer.is_valid():
            tags = request.data.get('tags', [])
            temp_tags = []
            for tag_name in tags:
                try:
                    tag = Tags.objects.get(id=tag_name)
                    temp_tags.append(tag)
                except Tags.DoesNotExist:
                    return Response({"error": f"Tag '{tag_name}' does not exist"}, status=400)
            blog = serializer.save()
            blog.tags.set(temp_tags)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk, author=request.user)
        blog.delete()
        return Response(status=204)