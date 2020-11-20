from django.shortcuts import render
from django.http import HttpResponse
from bson import ObjectId

from articleApp.models import Articleinfo
from django.views.decorators.csrf import csrf_exempt

from bs4 import BeautifulSoup as soup
from newspaper import Config
from lxml.etree import ParseError
from lxml.etree import ParserError
from urllib.request import urlopen
from newspaper import Article
from readability import Document
import re
# Create your views here.

@csrf_exempt
def add_article(request):

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent

    Website = request.POST.get("Website")
    op = urlopen(str(Website))
    rd = op.read()
    op.close()
    sp_page = soup(rd, 'xml')
    news_list = sp_page.find_all('item')
    urls = []
    titles = []

    for news in news_list:
        titles.append(news.title.text)
        urls.append(news.link.text)

    for i in range(len(news_list)):
        try:
            article = Article(urls[i], config=config )
            article.download()
            article.parse()
            doc = Document(article.text)
            cleanme = doc.summary()
            var = re.sub('<.*?>', '', cleanme)
            clean_article = Articleinfo(Website=request.POST.get("Website"),Title= str(titles[i]),
                          Authors = article.authors,Publish_Date = str(article.publish_date),
                          Article = var, URL = str(urls[i]))
            print(Website)
            clean_article.save()
        except (ParserError, ParseError,etree.ParserError):
            continue


    return HttpResponse("Inserted")

def get_article(request, keywords):
    compatible_articles = []
    allArticls = Articleinfo.objects.all()
    for article in allArticls:
        if keywords in article.Article:
            compatible_articles.append(article.Article)

    return HttpResponse(compatible_articles)
