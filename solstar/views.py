from django.shortcuts import render

def index(request):
    return render(request, 'solstar/index.html')



def collection(request):
    return render(request, 'solstar/collection.html')