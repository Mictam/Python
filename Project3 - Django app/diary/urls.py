from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add', views.addNote, name='add'),
    path('delete/<note_id>',views.deleteNote, name='delete'),
    path('edit/<note_id>',views.editNote,name='edit'),
    path('saveedited/<note_id>',views.saveedited,name='saveedited')
]