from django.shortcuts import render
from .models import Note, NoteList 

N = NoteList()

# Create your views here.
def base (request):
    return render(request, 'mis_notas/base.html')

def home(request):
    return render(request, 'mis_notas/home.html')

def notes(request):
    return render(request, 'mis_notas/notas.html', {'notas': N.note_list})

def create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    important = request.POST.get('important')

    if title == ''  or description == '':
        mensaje = 'Campos vacíos'
    else:
        if important:
            important = True
        else:
            important = False
        n = Note(title, description, important)
        mensaje = N.AgregarNota(n)
    
    return render(request, 'mis_notas/messages.html', {'mensaje' : mensaje})

def delete(request, title):
    mensaje = N.EliminarNota(title)
    return render(request, 'mis_notas/messages.html', {'mensaje' : mensaje})