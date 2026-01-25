from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404

@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # logic for editing...
    return render(request, 'bookshelf/edit_article.html', {'article': article})