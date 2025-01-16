from django.shortcuts import render, get_object_or_404
from blogs.serializers import BlogSerializer
from blogs.models import Blog, Tags, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.pagination import PageNumberPagination
from .filters import BlogFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class BlogDetails(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

            
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
        return Response({"message" : "blog deleted successfully"} , status=204)
    
class BlogListView(APIView):
    filter_backends = [DjangoFilterBackend , SearchFilter]
    filterset_class = BlogFilter
    search_fields = ['title', 'content', 'author__username', 'category__name', 'tags__name']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        blogs = Blog.objects.all()
        filtered_blogs = self.filter_queryset(blogs)
        result_page = paginator.paginate_queryset(filtered_blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def filter_queryset(self, queryset):
        filter_backends = [DjangoFilterBackend , SearchFilter]
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

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
