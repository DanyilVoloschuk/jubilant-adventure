from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from .models import Article, Street
from .forms import SearchForm
from django.utils import timezone


def cancel(request, article_id=1):
    return HttpResponseRedirect('/articles')


def index(request):
    last_person_added = Article.objects.all()[0:15]
    return render(request, 'articles/list.html',
                  {
                      'last_person_added': last_person_added,
                      'form': SearchForm(),
                   })


def search(request):
    print(request.POST)
    try:
        s = SearchForm(request.POST)
        if s.is_valid():
            p = Street.objects.filter(name=s.cleaned_data['your_name'])[0].article_set.all()
    except:
        p = ''
    return render(request, 'articles/search_description.html', {'persons': p, 'form': SearchForm(), 'req_name': s.cleaned_data['your_name']})


def add_new_btn(request):
    s = Street.objects.all()
    return render(request, 'articles/add_menu.html', {'streets': s})


def add_new_confirm(request):
    s = Street.objects.filter(name=request.POST['DropDownMenu'])
    person = Article(
        name=request.POST['FirstName'],
        street=s[0],
    )
    person.save()
    return HttpResponseRedirect('/articles')


def edit_btn(request, article_id):
    a = Article.objects.filter(id=article_id)
    s = Street.objects.all()
    return render(request, 'articles/edit_menu.html', {'person': a[0], 'streets': s})


def edit_confirm(request, article_id):
    post_data = request.POST
    first_name = post_data.get('FirstName')
    street_id = post_data.get('DropDownMenu')
    a = Article.objects.filter(id=article_id)
    a.update(name=first_name, street_id=street_id)
    return HttpResponseRedirect('/articles')


def delete_btn(request, article_id):
    a = Article.objects.filter(id=article_id)
    return render(request, 'delete_menu.html', {'person': a[0]})


def delete_confirm(request, article_id):
    a = Article.objects.filter(id=article_id)
    b = a[0].name
    a.delete()
    return render(request, 'congratulations.html', {'person': b})


def delete_congrat(request, article_id):
    a = Article.objects.filter(id=article_id)
    a.delete()
    return HttpResponseRedirect('/articles')
