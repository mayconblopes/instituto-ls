from django.shortcuts import render

from instituto_ls.models import Feedback, Hero, Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def quem_somos(request):
    heroes = Hero.objects.all()
    feedbacks = Feedback.objects.all().first()
    return render(request, 'quem_somos.html', { 
                                                'heroes': heroes,
                                                'feedbacks': feedbacks,
                                                })

def nosso_estudio(request):
    return render(request, 'nosso_estudio.html')