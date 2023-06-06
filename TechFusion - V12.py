# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
from datetime import datetime
import os

'''' PROYECTO POO 2023-1S
Fernando Ospina | Grupo de clase 10

Grupo de proyecto 4:
Alan Ryan Cheyne Gomez
Carlos Fernando Soriano Macana
Tuli Peña Melo
Valentina Giraldo Betancourt
'''

class Participantes:

    # Nombre de la base de datos  y ruta
    path = r'C:\Users\Alan\Code\Proyects\POO'
    db_name = path + r'/Participantes.db'
    actualiza = None
    def __init__(self, master=None):
        # Top Level - Ventana Principal
        self.win = tk.Tk() if master is None else tk.Toplevel()
        
        # Llamado a la rutina de centrado de pantalla
        self.centra(self.win,900,480)

        # Crear tabla en la base de datos
        self.crear_Tabla()
        
        # Top Level - Configuración
        self.win.configure(background="#d9f0f9", height="480", relief="flat", width="1024")
        self.win.geometry("1024x480")
        self.icon_path = os.path.join(self.path, 'f2.ico')
        self.win.iconbitmap(self.icon_path)
        self.win.resizable(False, False)
        self.win.title("Conferencia TechFusion")
        self.win.pack_propagate(0) 
        
        # Main widget
        self.mainwindow = self.win
        
        # Label Frame que dice Inscripcion
        self.lblfrm_Datos = tk.LabelFrame(self.win, width= 600, height= 200, labelanchor= "n", 
                                          font= ("Helvetica", 13,"bold"))
        
        # Label que dice Id
        self.lblId = ttk.Label(self.lblfrm_Datos)
        self.lblId.configure(anchor="e", font="TkTextFont", justify="left", text="Identificación")
        self.lblId.configure(width="12")
        self.lblId.grid(column="0", padx="5", pady="15", row="0", sticky="w")
        
        # Entry Id
        self.entryId = tk.Entry(self.lblfrm_Datos, validate="key", validatecommand=(self.win.register(lambda string: string.isdecimal()), "%S"))
        self.entryId.configure(exportselection="false", justify="left",relief="groove", takefocus=True, width="30")
        self.entryId.grid(column="1", row="0", sticky="w")
        self.entryId.bind("<KeyRelease>", self.valida_Id_Largo)
        self.entryId.bind("<BackSpace>", lambda _:self.entryId.delete(len(self.entryId.get()),'end'))
        
        # Label que dice Nombre
        self.lblNombre = ttk.Label(self.lblfrm_Datos)
        self.lblNombre.configure(anchor="e", font="TkTextFont", justify="left", text="Nombre")
        self.lblNombre.configure(width="12")
        self.lblNombre.grid(column="0", padx="5", pady="15", row="1", sticky="w")
        
        # Entry Nombre
        self.entryNombre = tk.Entry(self.lblfrm_Datos)
        self.entryNombre.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryNombre.grid(column="1", row="1", sticky="w")
        
        # Label que dice Direccion
        self.lblDireccion = ttk.Label(self.lblfrm_Datos)
        self.lblDireccion.configure(anchor="e", font="TkTextFont", justify="left", text="Dirección")
        self.lblDireccion.configure(width="12")
        self.lblDireccion.grid(column="0", padx="5", pady="15", row="2", sticky="w")
        
        # Entry Direccion
        self.entryDireccion = tk.Entry(self.lblfrm_Datos)
        self.entryDireccion.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryDireccion.grid(column="1", row="2", sticky="w")
        
        # Label que dice Celular
        self.lblCelular = ttk.Label(self.lblfrm_Datos)
        self.lblCelular.configure(anchor="e", font="TkTextFont", justify="left", text="Celular")
        self.lblCelular.configure(width="12")
        self.lblCelular.grid(column="0", padx="5", pady="15", row="3", sticky="w")
        
        # Entry Celular
        self.entryCelular = tk.Entry(self.lblfrm_Datos)
        self.entryCelular.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryCelular.grid(column="1", row="3", sticky="w")
        
        # Label que dice Entidad
        self.lblEntidad = ttk.Label(self.lblfrm_Datos)
        self.lblEntidad.configure(anchor="e", font="TkTextFont", justify="left", text="Entidad")
        self.lblEntidad.configure(width="12")
        self.lblEntidad.grid(column="0", padx="5", pady="15", row="4", sticky="w")
        
        # Entry Entidad
        self.entryEntidad = tk.Entry(self.lblfrm_Datos)
        self.entryEntidad.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryEntidad.grid(column="1", row="4", sticky="w")
        
        # Label que dice Fecha
        self.lblFecha = ttk.Label(self.lblfrm_Datos)
        self.lblFecha.configure(anchor="e", font="TkTextFont", justify="left", text="Fecha")
        self.lblFecha.configure(width="12")
        self.lblFecha.grid(column="0", padx="5", pady="15", row="5", sticky="w")
        
        # Entry Fecha
        self.entryFecha = tk.Entry(self.lblfrm_Datos)
        self.entryFecha.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryFecha.grid(column="1", row="5", sticky="w")
        self.entryFecha.bind("<KeyRelease>", self.formato_Fecha)
        self.entryFecha.bind("<BackSpace>", self.borra_Fecha)
          
        # Configuración del Label que dice Inscripción
        self.lblfrm_Datos.configure(height="310", relief="groove", text=" Inscripción ", width="330")
        self.lblfrm_Datos.place(anchor="nw", relx="0.01", rely="0.1", width="280", x="0", y="0")
        self.lblfrm_Datos.grid_propagate(0)
        
        # Botón Grabar
        self.btnGrabar = ttk.Button(self.win)
        self.btnGrabar.configure(state="normal", text="Grabar", width="9")
        self.btnGrabar.place(anchor="nw", relx="0.01", rely="0.75", x="0", y="0")
        self.btnGrabar.bind("<1>", self.adiciona_Registro, add="+")
        
        # Botón Editar
        self.btnEditar = ttk.Button(self.win)        
        self.btnEditar.configure(text="Editar", width="9")
        self.btnEditar.place(anchor="nw", rely="0.75", x="80", y="0")
        self.btnEditar.bind("<1>", self.edita_tablaTreeView, add="+")
        
        # Botón Eliminar
        self.btnEliminar = ttk.Button(self.win)
        self.btnEliminar.configure(text="Eliminar", width="9")
        self.btnEliminar.place(anchor="nw", rely="0.75", x="152", y="0")
        self.btnEliminar.bind("<1>", self.elimina_Registro, add="+")
        
        # Botón Cancelar
        self.btnCancelar = ttk.Button(self.win)
        self.btnCancelar.configure(text="Cancelar", width="9",command = self.limpia_Campos)
        self.btnCancelar.place(anchor="nw", rely="0.75", x="225", y="0")
        
        # Estilos que se usarán para el TreeView
        self.style = ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background='AliceBlue', font=('Calibri Light',10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
        self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])

        # Creación del TreeView llamado treeDatos
        self.treeDatos = ttk.Treeview(self.win, height = 10, style="estilo.Treeview", show="headings")
        self.treeDatos.place(x=380, y=10, height=340, width = 500)
        self.treeDatos.bind('<Double-Button-1>', self.edita_tablaTreeView)

        # Etiquetas de las columnas
        self.treeDatos["columns"] = ("Id", "Nombre", "Dirección", "Celular", "Entidad", "Fecha")
 
        # Encabezados de las columnas de la pantalla
        self.treeDatos.heading("Id", text="Id")
        self.treeDatos.heading("Nombre", text="Nombre")
        self.treeDatos.heading("Dirección", text="Dirección")   
        self.treeDatos.heading("Celular", text="Celular")
        self.treeDatos.heading("Entidad", text="Entidad")
        self.treeDatos.heading("Fecha", text="Fecha")

        # Anchos de las columnas
        self.treeDatos.column("Id", width=120)
        self.treeDatos.column("Nombre", width=120)
        self.treeDatos.column("Dirección", width=120)
        self.treeDatos.column("Celular", width=100)
        self.treeDatos.column("Entidad", width=120)
        self.treeDatos.column("Fecha", width=120)

        # Scrollbar en el eje Y de treeDatos
        self.scrollbar = ttk.Scrollbar(self.win, orient='vertical', command=self.treeDatos.yview)
        self.treeDatos.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(x=1000, y=50, height=400)

        # Carga los datos en treeDatos
        self.lee_tablaTreeView()    
        self.treeDatos.place(anchor="nw", height="400", rely="0.1", width="700", x="300", y="0")
 
    def centra(self,win,ancho,alto): 
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2 
        y = win.winfo_screenheight() // 2 - alto // 2 
        win.geometry(f'{ancho}x{alto}+{x}+{y}') 
        win.deiconify() 

    def run(self):
        self.mainwindow.mainloop()

    def valida_Id_Vacia(self):
        '''Valida que el Id no esté vacio, devuelve True si ok'''
        return (len(self.entryId.get()) != 0 )   

    def valida_Id_Largo(self, event=None):
        '''Valida que el Id no sea mayor a 15 caracteres'''
        if len(self.entryId.get()) > 15:
            self.entryId.delete(15, tk.END)
            mssg.showinfo('Alto', f'No puede ingresar más de 15 caracteres en el Id.')

    def valida_Id_Repetida(self):
        '''Valida que el Id ingresado no este previamente ingresado'''
        query = "SELECT * FROM t_participantes ORDER BY Id ASC"
        tuplas = self.run_Query(query)
        
        for tupla in tuplas:
            if str(tupla[0]) == self.entryId.get():
                return True

    def valida_Fecha(self, event=None):
        '''Valida que la fecha sea válida'''
        fecha_str = self.entryFecha.get()
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            es_bisiesto = fecha.year % 4 == 0 and (fecha.year % 100 != 0 or fecha.year % 400 == 0)
            if fecha.year >= 1 and 1 <= fecha.month <= 12 and 1 <= fecha.day <= (29 if es_bisiesto and fecha.month == 2 else 28):
                return True
            else:
                return False
        except ValueError:
            return False

    def formato_Fecha(self, event=None):
        '''Valida que la fecha no sea mayor a 10 caracteres y agrega los slash'''

        # Agrega los slash
        fecha_str = self.entryFecha.get()
        if len(fecha_str) == 2:
            self.entryFecha.insert(tk.END, '/')
        elif len(fecha_str) == 5:
            self.entryFecha.insert(tk.END, '/')
        
        # Impide que se ingresen más de 10 caracteres
        if len(self.entryFecha.get()) > 10:
            self.entryFecha.delete(10, tk.END)

    def borra_Fecha(self, event=None):
        '''Función unida a la tecla de backspace en el entry Fecha
        Borra una vez cada número y dos veces si encuentra un slash'''
        if len(self.entryFecha.get()) == 3 or len(self.entryFecha.get()) == 6:
            self.entryFecha.delete(len(self.entryFecha.get())-1,'end')
        else:
            self.entryFecha.delete(len(self.entryFecha.get()),'end')

    def carga_Datos(self):
        # Obtiene el registro seleccionado en la TreeView
        seleccion = self.treeDatos.selection()
        datos_registro = self.treeDatos.item(seleccion)['values']

        # Asigna los datos a los Entry correspondientes
        self.entryId.delete(0, 'end')
        self.entryId.insert(0, datos_registro[0])
        self.entryId.configure(state='readonly')
        self.entryNombre.delete(0, 'end')
        self.entryNombre.insert(0, datos_registro[1])
        self.entryDireccion.delete(0, 'end')
        self.entryDireccion.insert(0, datos_registro[2])
        self.entryCelular.delete(0, 'end')
        self.entryCelular.insert(0, datos_registro[3])
        self.entryEntidad.delete(0, 'end')
        self.entryEntidad.insert(0, datos_registro[4])
        self.entryFecha.delete(0, 'end')
        self.entryFecha.insert(0, datos_registro[5])

              
    def limpia_Campos(self):
      '''Borra el texto que esté en todos los entries'''
      self.entryId.configure(state='normal')
      self.entryId.delete(0,tk.END)
      self.entryNombre.delete(0,tk.END)
      self.entryDireccion.delete(0,tk.END)
      self.entryCelular.delete(0,tk.END)
      self.entryEntidad.delete(0,tk.END)
      self.entryFecha.delete(0,tk.END)

    def run_Query(self, query, parametros = ()):
        '''Función para ejecutar los Querys a la base de datos'''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def lee_tablaTreeView(self):
        '''Lee los datos de la tabla t_participantes y los muestra en el TreeView'''

        # Borra los elementos existentes en el TreeView
        self.treeDatos.delete(*self.treeDatos.get_children())

        # Consulta la tabla t_participantes de la base de datos
        query = "SELECT * FROM t_participantes ORDER BY Id ASC"
        tuplas = self.run_Query(query)

        # Agrega los registros de la búsqueda al Treeview
        for tupla in tuplas:
            self.treeDatos.insert("", "end", values=tupla)

    def crear_Tabla(self):
       '''Crea la tabla t_participantes la base de datos si no está creada aún'''
       query = 'CREATE TABLE IF NOT EXISTS t_participantes(Id INT, Nombre TEXT, Dirección TEXT, Celular INT, Entidad TEXT, Fecha TEXT)'
       self.run_Query(query)
            
    def adiciona_Registro(self, event=None):
        '''Si la variable actualiza es True entonces actualiza un registro que ya existe en la base de datos
        Si la variable actualiza no es True entonces crea un nuevo registro en la base de datos
        Adiciona un registro a la base de datos si pasa todas las validaciones'''
        if self.valida_Fecha():
            if self.actualiza:
                self.actualiza = None
                self.entryId.configure(state = 'normal')
                query = 'UPDATE t_participantes SET Id = ?,Nombre = ?,Dirección = ?,Celular = ?, Entidad = ?, Fecha = ? WHERE Id = ?'
                parametros = (self.entryId.get(), self.entryNombre.get(), self.entryDireccion.get(),
                            self.entryCelular.get(), self.entryEntidad.get(), self.entryFecha.get(), self.entryId.get())
                self.run_Query(query, parametros)
                mssg.showinfo('Ok', f'Registro {self.entryId.get()} actualizado con éxito.')
                self.limpia_Campos()
            else:
                query = 'INSERT INTO t_participantes VALUES(?, ?, ?, ?, ?, ?)'
                parametros = (self.entryId.get(),self.entryNombre.get(), self.entryDireccion.get(),
                            self.entryCelular.get(), self.entryEntidad.get(), self.entryFecha.get())
                if self.valida_Id_Vacia():
                    if self.valida_Id_Repetida():
                        mssg.showerror("¡Atención!","No puede ingresar una identificación existente")                 
                    else:
                        self.run_Query(query, parametros)
                        mssg.showinfo('Ok', f'Registro {self.entryId.get()} agregado.')
                        self.limpia_Campos()
                else:
                    mssg.showerror("¡Atención!","No puede dejar la identificación vacía")
            self.lee_tablaTreeView()
        else:
            mssg.showerror("¡Atención!","La fecha no es válida.")

    def edita_tablaTreeView(self, event=None):
        '''Función que se activa cuando presionas doble click en un registro
        del TreeView o cuando seleccionas un registro y presionas Editar'''
        try:
            # Carga los campos desde la tabla TreeView
            self.treeDatos.item(self.treeDatos.selection())['text']
            self.limpia_Campos()
            self.actualiza = True # Esta variable controla la actualización
            self.carga_Datos()
        except IndexError as error:
            self.actualiza = None
            mssg.showerror("¡Atención!",'Por favor seleccione un ítem de la tabla')
            return
        
    def elimina_Registro(self, event=None):
        try:
            query= "DELETE FROM t_participantes WHERE id=?"
            seleccion = self.treeDatos.selection()
            dic_seleccion = self.treeDatos.item(seleccion)['values']
            parametro = [dic_seleccion[0]]
            self.run_Query(query, parametro)
            self.treeDatos.delete(self.treeDatos.selection())
        except:
            for tupla in self.treeDatos.selection():
                query= "DELETE FROM t_participantes WHERE id=?"
                seleccion = (tupla,)
                dic_seleccion = self.treeDatos.item(seleccion)['values']
                parametro = [dic_seleccion[0]]
                self.run_Query(query, parametro)
                self.treeDatos.delete(tupla)
        

if __name__ == "__main__":
    app = Participantes()
    app.run() 