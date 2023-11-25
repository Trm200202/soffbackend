from rest_framework import serializers
from . import models
from datetime import  datetime

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ("id", "name")

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ("id",
                  "name")

class AdvantageListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Adventage
        fields = ("id",
                  "title",
                  "tags",
                  "poster")

class AdventageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Adventage
        fields = ("title",
                  "body",
                  )

class ArticleListSerializer(serializers.ModelSerializer):
    diff = serializers.SerializerMethodField(method_name="difference")
    tags = TagSerializer()
    category = CategorySerializer()
    author = AuthorSerializer()


    def difference(self, obj):
        result = obj.created_at
        r  = datetime.now().date() - result
        return r
    
    


    class Meta:

        model = models.Article
        fields = ("id",
                  "poster",
                  "title",
                  "category",
                  "tags",
                  "created_at",
                  "author",
                  "diff", 
                  )


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()


    class Meta:
        model = models.Article
        fields = ("body",
                  "author",
                  )



class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ("id",
                  "name",
                  "order",
                  "imagex")


class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ("name",
                  "body",
                  )


class ApplicationFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ApplicationForm
        fields = ("full_name",
                  "phone_number",
                  )




        
class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gallery
        fields = ("title",
                  "image",
                  )


class CategoryWithCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return models.Article.objects.filter(category=obj).count()

    class Meta:
        model = models.Category
        fields = ("id", 'name', "count", )

class Way2JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Way2Job
        fields = "__all__"

class GalleryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gallery
        fields = ("id",
                  "title",
                  "image",
                  )