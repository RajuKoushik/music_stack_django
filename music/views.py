from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from . import views
# Create your views here.
from django.http import HttpResponse
from .models import Album, Song

def index(request):
    return HttpResponse("<h1>This is the music app homepage .</h1>")

def details(request , albums_id):
    try:
        album = Album.objects.get(pk=albums_id)
    except Album.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'music/details.html', {'album': album})







