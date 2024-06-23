from django.shortcuts import render, redirect
from openai import OpenAI
from .models import Article
from .forms import ArticleForm
from django.http import JsonResponse
from django.utils import translation
from django.conf import settings
from haystack.query import SearchQuerySet
client = OpenAI(api_key=settings.OPENAI_API_KEY)



def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = client.completions.create(model="gpt-3.5-turbo",
        prompt=question,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7)
        answer = response.choices[0].text.strip()
        return JsonResponse({'answer': answer})
    return render(request, 'main/chatbot.html')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = SearchQuerySet().filter(content=query)
        gpt_response = client.completions.create(engine="text-davinci-003",
        prompt=f"Based on these articles, provide a summary for the search query: {query}\n\n" + "\n".join([f"Title: {result.object.title}, Content: {result.object.content}" for result in results]),
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7)
        gpt_summary = gpt_response.choices[0].text.strip()
        return render(request, 'main/search_results.html', {'results': results, 'query': query, 'gpt_summary': gpt_summary})
    return render(request, 'main/search_results.html', {'results': results, 'query': query})

def article_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/article_liste.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            if request.is_ajax():
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
            if request.is_ajax():
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ArticleForm()
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'main/add_article.html', {'form': form, 'articles': articles})

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article_list')
def change_language(request, language):
    if language in ['en', 'fr','es']:
        translation.activate(language)
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

   