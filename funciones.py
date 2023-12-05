from tkinter import *

def agregar_tarea(lista_tareas, tarea):
    lista_tareas.insert("end", tarea)

def eliminar_tarea(lista_tareas, index):
    lista_tareas.delete(index)
