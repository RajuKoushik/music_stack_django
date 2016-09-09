from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from . import views
# Create your views here.
from django.http import HttpResponse
from .models import Album, Song
from django.template import RequestContext, loader

def index(request):
    album_list = Album.objects.all()

    template = loader.get_template('music/index.html')
    context = RequestContext(request, {'album_list': album_list,})
    # the context is a dictionary mapping template variable names to python objects
    return HttpResponse(template.render(context))




def details(request , albums_id):
    try:
        album = Album.objects.get(pk=albums_id)
    except Album.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'music/details.html', {'album': album})







