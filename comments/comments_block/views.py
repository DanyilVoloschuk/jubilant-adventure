from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache

from .models import Comment
from .serializers import CommentSerializer

import logging
logger = logging.getLogger('django')


class CommentView(APIView):

    @method_decorator(cache_page(5))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        print(request.method, request.data)
        comments = Comment.objects.all()
        serialized = CommentSerializer(comments, many=True)
        cache.clear()
        return Response(serialized.data)

    def post(self, request, format=None):
        #print(request.method, request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        print(request.method, request.data)
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(request.method, request.data)
        pk = int(request.data['pk'][0])
        print(pk)
        comment = Comment.objects.get(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentDetail(APIView):
    @csrf_exempt
    def get_object(selfself, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        print(request.method, request.data)
        comment = self.get_object()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cache.clear()
        print(request.method, request.data, pk)
        if request.data['comment_text']:
            comment = self.get_object(pk)
            print(comment.comment_text, request.data['comment_text'])
            logger.info(f'{pk} comment has been changed from "{comment.comment_text}" to "{request.data["comment_text"]}')
            comment.comment_text = request.data['comment_text']

            comment.save()

            print(comment.comment_text, request.data['comment_text'])
            return Response(status=status.HTTP_200_OK)
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        print(request.method, request.data)
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def index(request):
    return render(request, 'base.html')
