from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from accountapp.models import Comment
from accountapp.serializers import CommentSerializer

# https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
@csrf_exempt
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

@csrf_exempt
def comment_detail(request,pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        comment.delete()
        return HttpResponse(status=204)