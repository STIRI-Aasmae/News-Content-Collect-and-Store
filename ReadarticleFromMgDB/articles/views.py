from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from articles.models import Articleinfo
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def article_byKW(request):
    #here we search articles that contain a keyword
    if request.method == 'GET':
        articles = Articleinfo.objects.all()
        # we get the keyword from the request ex: http://127.0.0.1:8087/api/articless?Article=keyword
        Article = request.GET.get('Article', None)
        if Article is not None:
            # we filter all the articles that contains that keyword
            articles = articles.filter(Article__icontains=Article)
        articles_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)


