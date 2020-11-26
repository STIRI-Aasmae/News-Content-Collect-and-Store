from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^api/articless$', views.article_byKW),
]