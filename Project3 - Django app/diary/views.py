from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Note
from .forms import NoteForm,EditForm
# Create your views here.

def index(request):
    note_list = Note.objects.order_by('date_id')

    form = NoteForm()

    context = {'note_list' : note_list,'form' : form}
    return render(request,'diary/index.html',context)

@require_POST
def addNote(request):
    form = NoteForm(request.POST)
    print(request.POST['date_id'])
    print(request.POST['content'])

    input_date = request.POST['date_id']
    input_content = request.POST['content']

    new_note = Note(date_id=input_date,content=input_content)    
    new_note.save()
        

    return redirect('index')

def deleteNote(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()

    return redirect('index')

@require_POST
def saveedited(request,note_id):
    note_old = Note.objects.get(pk=note_id)
    text = request.POST['content']
    note_new = Note(date_id=note_old.date_id,content=text)
    note_old.delete()
    note_new.save()
    
    return redirect('index')


def editNote(request,note_id):
    form = EditForm(request.POST)
    note = Note.objects.get(pk=note_id)
    print(note.date_id)
    

    form = EditForm(initial={'content': note.content})

    context = {'form': form, 'note': note}
    

    return render(request,'diary/edit.html',context)