from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    ListView
)

# Create your views here.
from .models import Article, Comment
from .forms import CommentModelForm

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(post_id=id)
    comment_form = CommentModelForm(request.POST or None)
    if comment_form.is_valid():
        comment_form.post_id = id
        comment_form.save()
        comment_form = CommentModelForm()
    context = {
        'object': obj,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'articles/article_detail.html', context)


