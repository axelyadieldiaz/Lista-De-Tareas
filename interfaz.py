from tkinter import *
# from tkinter import ttk
from config import *
from funciones import *

class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")
        self.root.config(bg=COLOR_PRINCIPAL)

        self.lista_tareas = Listbox(self.root, bg="white", font=("Arial", TAMANO_FUENTE))
        self.lista_tareas.pack(pady=10)

        self.entry_tarea = Entry(self.root, font=("Arial", TAMANO_FUENTE))
        self.entry_tarea.pack(pady=10)

        self.btn_agregar = Button(self.root, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        self.btn_eliminar = Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            agregar_tarea(self.lista_tareas, tarea)
            self.entry_tarea.delete(0, END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            eliminar_tarea(self.lista_tareas, seleccion)
