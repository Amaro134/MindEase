from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def article_list(request):
    # Fetch only published articles
    articles = Article.objects.filter(is_published=True)
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'article_detail.html', {'article': article})

@login_required
def upload_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.is_published = True  # Mark the article as published
            article.save()
            messages.success(request, "Article published successfully!")
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'upload_article.html', {'form': form})
def mood_tips(request):
    return render(request, 'mood_tips.html')
