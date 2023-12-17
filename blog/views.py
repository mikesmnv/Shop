from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .models import Article

POSTS_PER_PAGE = 4


# def home(request):
#     posts = Article.objects.all()
#     res = '<h1>Список товаров</h1>'
#     for post in posts:
#         res += f'<div><h3>{post.title}</h3><div>{post.photo}</div><div>Цена: {post.price}</div></div><hr>'
#     return HttpResponse(res)


def home(request):
    page_number = int(request.GET.get('page', 1))
    posts = Article.objects.all()
    pagi = Paginator(posts, POSTS_PER_PAGE)
    next_page, previos_page = None, None
    page_posts = pagi.get_page(page_number)

    if page_posts.has_next():
        next_page = page_posts.next_page_number()
    if page_posts.has_previous():
        previos_page = page_posts.previous_page_number()

    context = {'posts': page_posts,
               'pages': pagi.num_pages,
               'current_page': page_number,
               'next_page': next_page,
               'previos_page': previos_page}

    return render(request, "blog/home.html", context)


def shop(request):
    items = Article.objects.all()
    context = {'items': items}
    return render(request, "blog/index.html", context)
