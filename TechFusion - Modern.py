# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Participantes:

    # Nombre de la base de datos  y ruta 
    path = r'C:\Users\Alan\Code\Proyects\POO'
    db_name = path + r'/Participantes.db'
    actualiza = None
    def __init__(self, master=None):
        # Top Level - Ventana Principal
        self.win = ctk.CTk() if master is None else tk.Toplevel()
        
        # Llamado a la rutina de centrado de pantalla
        self.centra(self.win,900,480)

        # Crear tabla en la base de datos
        self.crear_Tabla()
        
        # Top Level - Configuración
        self.win.configure(background="#d9f0f9", height="480", relief="flat", width="1024")
        self.win.geometry("1024x480")
        self.icon_path = self.path + r'/f2.ico'
        self.win.iconbitmap(self.icon_path)
        self.win.resizable(False, False)
        self.win.title("Conferencia TechFusion")
        self.win.pack_propagate(0) 
        
        # Main widget
        self.mainwindow = self.win
        # Label Frame Modificado
        self.lblfrm_Datos = ctk.CTkFrame(self.win,width= 200, height= 600, corner_radius=10)
        self.lblfrm_Datos.place(relx="0.01", rely="0.15", anchor="nw")
        #Titulo Modificado
        self.logo_label = ctk.CTkLabel(self.win, text="Inscripción", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(padx=100, pady=42)
        # Label que dice Frame
        #self.lblfrm_Datos = tk.LabelFrame(self.win, width= 600, height= 200, labelanchor= "n", font= ("Helvetica", 13,"bold")) 
        #self.lblfrm_Datos.configure(height="310", relief="groove", text=" Inscripción ", width="330")
        #self.lblfrm_Datos.place(anchor="nw", relx="0.01", rely="0.1", width="280", x="0", y="0")
        #self.lblfrm_Datos.grid_propagate(0)
        
        # Label que dice Id
        self.lblId = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblId.configure(anchor="e", justify="left", text="Idenficación")
        #self.lblId.configure(width="12")
        self.lblId.grid(column="0", padx="5", pady="8", row="0", sticky="e")
        
        # Entry Id
        self.entryId = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10)
        #self.entryId.configure(exportselection="false", justify="left",relief="groove", takefocus=True, width="30")
        self.entryId.grid(column="1", row="0", sticky="w")
        self.entryId.bind("<Key>", self.valida_Identificacion)
        self.entryId.bind("<BackSpace>", lambda _:self.entryId.delete(len(self.entryId.get()),'end'))
        
        # Label que dice Nombre
        self.lblNombre = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblNombre.configure(anchor="e", justify="left", text="Nombre")
        #self.lblNombre.configure(width="12")
        self.lblNombre.grid(column="0", padx="5", pady="8", row="1", sticky="e")
        
        # Entry Nombre
        self.entryNombre = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10) 
        self.entryNombre.grid(column="1", row="1", sticky="e")
        
        # Label que dice Direccion
        self.lblDireccion = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblDireccion.configure(anchor="e", justify="left", text="Dirección")
        #self.lblDireccion.configure(width="12")
        self.lblDireccion.grid(column="0", padx="5", pady="8", row="2", sticky="e")
        
        # Entry Direccion
        self.entryDireccion = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10)
        #self.entryDireccion.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryDireccion.grid(column="1", row="2", sticky="w")
        
        # Label que dice Celular
        self.lblCelular = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblCelular.configure(anchor="e", justify="left", text="Celular")
        #self.lblCelular.configure(width="12")
        self.lblCelular.grid(column="0", padx="5", pady="8", row="3", sticky="e")
        
        # Entry Celular
        self.entryCelular = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10)
        #self.entryCelular.configure(exportselection="false", justify="left",relief="groove", width="30")
        self.entryCelular.grid(column="1", row="3", sticky="e")
        
        # Label que dice Entidad
        self.lblEntidad = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblEntidad.configure(anchor="e", justify="left", text="Entidad")
        #self.lblEntidad.configure(width="12")
        self.lblEntidad.grid(column="0", padx="5", pady="8", row="4", sticky="e")
        
        # Entry Entidad
        self.entryEntidad = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10)
        #self.entryEntidad.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryEntidad.grid(column="1", row="4", sticky="w")
        
        # Label que dice Fecha
        self.lblFecha = ctk.CTkLabel(self.lblfrm_Datos)
        self.lblFecha.configure(anchor="e", justify="left", text="Fecha")
        #self.lblFecha.configure(width="12")
        self.lblFecha.grid(column="0", padx="5", pady="8", row="5", sticky="e")
        
        # Entry Fecha
        self.entryFecha = ctk.CTkEntry(self.lblfrm_Datos, width=200, height=25, border_width=2, corner_radius=10)
        #self.entryFecha.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryFecha.grid(column="1", row="5", sticky="w")
        self.entryFecha.bind("<Key>", self.valida_Fecha)
        self.entryFecha.bind("<BackSpace>",lambda _:self.entryFecha.delete(len(self.entryFecha.get()),'end'))
          

        # Botón Grabar
        #self.btnGrabar = ttk.Button(self.win)
        self.btnGrabar = ctk.CTkButton(self.win, width=60, height=32, border_width=0, corner_radius=5, text="Grabar")
        #self.btnGrabar.configure(state="normal", text="Grabar", width="9")
        self.btnGrabar.place(relx="0.01", rely="0.72", anchor="nw")
        self.btnGrabar.bind("<1>", self.adiciona_Registro, add="+")
        
        
        # Botón Editar
        #self.btnEditar = ttk.Button(self.win)
        self.btnEditar = ctk.CTkButton(self.win, width=60, height=32, border_width=0, corner_radius=5, text="Editar")
        #self.btnEditar.configure(text="Editar", width="9")
        self.btnEditar.place(relx="0.08", rely="0.72", anchor="nw")
        self.btnEditar.bind("<1>", self.edita_tablaTreeView, add="+")
        
        # Botón Eliminar
        self.btnEliminar = ctk.CTkButton(self.win, width=60, height=32, border_width=0, corner_radius=5, text="Eliminar")
        #self.btnEliminar.configure(text="Eliminar", width="9")
        self.btnEliminar.place(relx="0.152", rely="0.72", anchor="nw")
        self.btnEliminar.bind("<1>", self.elimina_Registro, add="+")
        
        # Botón Cancelar
        self.btnCancelar = ctk.CTkButton(self.win, width=60, height=32, border_width=0, corner_radius=5, text="Cancelar", command = self.limpia_Campos)
        #self.btnCancelar.configure(text="Cancelar", width="9",command = self.limpia_Campos)
        self.btnCancelar.place(relx="0.225", rely="0.72", anchor="nw")

        #Estilos Interfaz
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.win, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(padx=0.02, pady=320)
        
        # Estilos que se usarán para el TreeView
        self.style = ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background='AliceBlue', font=('Calibri Light',10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
        self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])

        # Creación del TreeView llamado treeDatos
        self.treeDatos = ttk.Treeview(self.win, height = 10, style="estilo.Treeview", show="headings")
        self.treeDatos.place(x=380, y=10, height=340, width = 500)

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

    def valida(self):
        '''Valida que el Id no esté vacio, devuelve True si ok'''
        return (len(self.entryId.get()) != 0 )   

    def run(self):
        self.mainwindow.mainloop()

    def valida_Identificacion(self, event=None):
      pass

    def valida_Fecha(self, event=None):
      
      pass
    

    def carga_Datos(self):
      '''Trae los datos de una tupla que ya existe cuando se quiere editar'''

      pass
              
    def limpia_Campos(self):
      '''Borra el texto que esté en todos los entries'''
      pass

    def run_Query(self, query, parametros = ()):
        '''Función para ejecutar los Querys a la base de datos'''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def lee_tablaTreeView(self):
        '''Lee los datos de la tabla t_participantes y los muestra en el TreeView'''

        # Consulta la tabla t_participantes de la base de datos
        query = "SELECT * FROM t_participantes ORDER BY Id DESC"
        tuplas = self.run_Query(query)

        # Agrega los registros a la Treeview
        for tupla in tuplas:
            self.treeDatos.insert("", "end", values=tupla)

    def crear_Tabla(self):
       query = 'CREATE TABLE IF NOT EXISTS t_participantes(Id INT, Nombre TEXT, Dirección TEXT, Celular INT, Entidad TEXT, Fecha TEXT)'
       self.run_Query(query)
            
    def adiciona_Registro(self, event=None):
        '''Adiciona un producto a la BD si la validación es True'''
        if self.actualiza:
            self.actualiza = None
            self.entryId.configure(state = 'readonly')
            query = 'UPDATE t_participantes SET Id = ?,Nombre = ?,Dirección = ?,Celular = ?, Entidad = ?, Fecha = ? WHERE Id = ?'
            parametros = (self.entryId.get(), self.entryNombre.get(), self.entryDireccion.get(),
                          self.entryCelular.get(), self.entryEntidad.get(), self.entryFecha.get()
                          )
                        #   self.entryId.get())
            self.run_Query(query, parametros)
            mssg.showinfo('Ok', f'Registro {self.entryId.get()} actualizado con éxito')
        else:
            query = 'INSERT INTO t_participantes VALUES(?, ?, ?, ?, ?, ?)'
            parametros = (self.entryId.get(),self.entryNombre.get(), self.entryDireccion.get(),
                          self.entryCelular.get(), self.entryEntidad.get(), self.entryFecha.get())
            if self.valida():
                self.run_Query(query, parametros)
                self.limpia_Campos()
                mssg.showinfo('', f'Registro {self.entryId.get()} agregado')
            else:
                mssg.showerror("¡Atención!","No puede dejar la identificación vacía")
        self.limpia_Campos()
        self.lee_tablaTreeView()

    def edita_tablaTreeView(self, event=None):
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
     pass
     #Cambio De estilos
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = Participantes()
    app.run() 