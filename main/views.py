from django.shortcuts import render, redirect
from openai import OpenAI
from .models import Article
from .models import QAPair,find_best_answer
from .forms import SearchForm,ArticleForm
from django.http import JsonResponse
from django.utils import translation
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from transformers import pipeline

client = OpenAI(api_key=settings.OPENAI_API_KEY)




@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        question = request.POST.get("question")
        qa_pairs = QAPair.objects.all()
        answer = find_best_answer(question, qa_pairs)
        return JsonResponse({"answer": answer})
    return render(request, 'main/chatbot.html')
    


def search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Initial filtering using Django ORM
            articles = Article.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            
            # Use the question-answering pipeline from Hugging Face
            qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
            refined_results = []
            for article in articles:
                result = qa_pipeline(question=query, context=article.content)
                if result['score'] > 0.2:  # Filter based on relevance score
                    refined_results.append((article, result['answer'], result['score']))

            # Sort results by relevance score
            refined_results = sorted(refined_results, key=lambda x: x[2], reverse=True)
            results = refined_results
    else:
        form = SearchForm()
    
    return render(request, 'main/search_results.html', {'form': form, 'query': query, 'results': results})



def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/article_liste.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'article': {
                        'id': article.id,
                        'title': article.title,
                        'content': article.content,
                        'publication_date': article.publication_date.strftime('%Y-%m-%d %H:%M:%S'),
                    }
                })
            return redirect('article_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = SearchForm()
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/add_article.html', {'form': form, 'articles': articles})

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article_list')
def change_language(request, language):
    if language in ['en', 'fr','es','de']:
        translation.activate(language)
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

   