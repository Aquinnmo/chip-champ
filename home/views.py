from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

def home(request):
    """Home page view"""
    context = {
        'title': 'Project Noble',
        'message': 'Virtual poker chip management for in-person Texas Hold Em games. Making poker more accessible to all.',
    }
    return render(request, 'home/home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Project Noble',
        'message': 'Learn more about our virtual poker chip management service.',
    }
    return render(request, 'home/about.html', context)

def page_detail(request, slug):
    """Dynamic page view"""
    page = get_object_or_404(Page, slug=slug, is_active=True)
    context = {
        'page': page,
        'title': page.title,
    }
    return render(request, 'home/page_detail.html', context)
