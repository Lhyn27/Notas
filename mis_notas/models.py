from django.db import models

# Create your models here.
class Note:
    def __init__(self, title, description, important = False) -> None:
        self.title = title
        self.description = description
        self.important = important
        
class NoteList:
    def __init__(self) -> None:
        self.note_list = []
        
    def BuscarNota(self, title):
        for n in self.note_list:
            if title == n.title:
                return n
        return None

    def AgregarNota(self, nota) -> str:
        if not isinstance(nota, Note):
            return 'Debe agregar una nota'

        result = self.BuscarNota(nota.title)

        if result is not None:
            return 'La nota ya existe'
        
        self.note_list.append(nota)
        return 'Nota agregada'
    
    def EliminarNota(self, title):
        result = self.BuscarNota(title)
        if result is not None:
            self.note_list.remove(result)
            return 'Libro eliminado'
        return 'Libro no encontrado'

    def ListarNotas(self):
        return self.note_list