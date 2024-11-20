from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Article

@permission_required('myapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('myapp.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # Form handling logic
        return redirect('article_list')
    return render(request, 'articles/create.html')

@permission_required('myapp.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Edit logic
        return redirect('article_list')
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('myapp.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
# Enforcing permissions using @permission_required
# Example: Only users with 'can_edit' permission can access article_edit view.
