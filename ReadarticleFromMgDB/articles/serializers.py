from rest_framework import serializers
from articles.models import Articleinfo

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articleinfo
        fields = ('id',
                'Website',
                 'Title',
                 'Authors',
                 'Publish_Date',
                 'Article',
                 'URL')