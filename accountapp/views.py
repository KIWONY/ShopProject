from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser

from accountapp.models import Comment
from accountapp.serializers import CommentSerializer


def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # https://www.django-rest-framework.org/api-guide/status-codes/#successful-2xx
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)