from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from accountapp.models import Comment
from accountapp.serializers import CommentSerializer


# https://www.django-rest-framework.org/api-guide/views/#class-based-views
class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)

        except Comment.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = self.get_object(id)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
# https://www.django-rest-framework.org/api-guide/views/#api_view
@api_view(["GET","POST"])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # https://www.django-rest-framework.org/api-guide/status-codes/#successful-2xx
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def comment_detail(request,pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)