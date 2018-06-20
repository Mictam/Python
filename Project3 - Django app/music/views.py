from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Song
from wsgiref.util import FileWrapper
import os
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import smart_str
from .forms import UploadFileForm

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)

        print(form.is_valid())

        if form.is_valid():
            file = Song(field=request.FILES['field'])
            print(request.FILES['field'])
            file.name= request.FILES['field']
            file.description="opis..."
            file.save()

            return HttpResponseRedirect(reverse('music'))
    else:
        form = UploadFileForm()

    songs = Song.objects.all()

    return render(request,'music/index.html',{'songs': songs, 'form': form})

def deleteSong(request,song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()

    return redirect('music')

def downloadSong(request,song_id):
    song = Song.objects.get(pk=song_id)
    filename = song.name
    response = HttpResponse(song.field,content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response