from django.urls import path
from .views import (
#    ArticleDetailView,
    article_detail_view,
    ArticleListView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', article_detail_view, name='article-detail')
#    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail')
]