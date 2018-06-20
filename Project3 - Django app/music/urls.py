from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index,name='music'),
    path('delete/<song_id>',views.deleteSong, name='delete'),
    path('download/<song_id>',views.downloadSong, name='download')
]
