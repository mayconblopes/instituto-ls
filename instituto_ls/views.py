from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def nosso_estudio(request):
    return render(request, 'nosso_estudio.html')