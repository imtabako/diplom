from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/about.html')


def receiving(request):
    return render(request, 'polls/receiving.html')


def unload(request):
    return render(request, 'polls/unload.html')