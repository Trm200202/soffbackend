from .views import *
from django.urls import path

urlpatterns = [
    path("advantage-list/", AdvantageListAPIView.as_view()),
    path("advantage-detail/<int:pk>/", AdvantageDetailAPIView.as_view()),
    path("article-list/", ArticleListAPIView.as_view()),
    path("article-detail/<int:pk>/", ArticleDetailAPIView.as_view()),
    path("course-list/", CourseListAPIView.as_view()),
    path("course-detail/", CourseListAPIView.as_view()),
    path("applicationform/", ApplicationFormAPIView.as_view()),
    path("tags/<int:pk>/", TagAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),
    path("Gallery/", GalleryAPIView.as_view()),
    path("category-with-count/", CategoryWithCountAPIView.as_view()),
    path("author-detail/<int:pk>/", AuthorDetailAPIView.as_view()),
    path("way2job/<int:pk>/", Way2JobAPIView.as_view()),
    path("gallery-detail/<int:pk>/", GalleryDetailAPIView.as_view())
    ]
