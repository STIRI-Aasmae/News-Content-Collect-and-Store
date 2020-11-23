from rest_framework import serializers
from articleApp.models import Articleinfo

class ArticleinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articleinfo
        fields = (
            "id",
            "Website",
            "Title",
            "Authors",
            "Publish_Date",
            "Article",
            "URL"
        )