from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

def home(request):
    """Home page view"""
    context = {
        'title': 'Chip Champ',
        'message': 'The first user-friendly virtual poker chip alternative for in-person Texas Hold \'Em games.',
    }
    return render(request, 'home/home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Chip Champ',
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

def custom_404_view(request, exception):
    """Custom 404 error page view"""
    return render(request, '404.html', status=404)
