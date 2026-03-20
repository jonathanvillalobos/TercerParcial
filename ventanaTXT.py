import tkinter as tk
from tkinter import messagebox

def guardar_archivo():
  nombre = entrada_nombre.get()
  contenido = cuadro_texto.get("1.0", tk. END)
  try:
      with open (nombre, "w") as archivo:
          archivo.write(contenido)
      messagebox. showinfo( "Éxito", "Archivo guardado correctamente")
  except:
    messagebox. showerror ("Error", "No se pudo guardar el archivo")

def abrir_archivo():
  nombre = entrada_nombre.get()
  
  try:
      with open (nombre, "r") as archivo:
          contenido = archivo.read()
          cuadro_texto.delete("1.0", tk.END)
          cuadro_texto.insert(tk.END, contenido)
  except FileNotFoundError:
    messagebox. showerror ("Error", "el archivo no existe")
    
def guardar_texto():
  nombre = entrada_nombre.get()
  contenido = cuadro_texto.get("1.0", tk. END)
  
  try: 
      with open(nombre, "a") as archivo:
          archivo.write(contenido)
      messagebox.showinfo("Exito", "Texto guardado correctamente")
  except:
      messagebox.showerror("Error", "No se pudo agregar el texto")
      
def limpiar_archivo():
    cuadro_texto.delete("1.0", tk.END)
    
#Ventana principal

ventana = tk.Tk()
ventana.title("Gestor de archivos de texto")
ventana.geometry("500x400")

#etiqueta nombre archivo
tk. Label(ventana, text="Nombre del Archivo:").grit(row=0, colimn=0, padx=10, pady=10)

entrada_nombre = tk. Entry(ventana, width=30)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

# Cuadro de texto
cuadro_texto = tk.Text(ventana, width=60, height=15)
cuadro_texto.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Botones
btn_guardar = tk.Button(ventana, text="Guardar", width=12, command=guardar_archivo)
btn_guardar.grid(row=2, column=0, pady=10)

btn_abrir = tk.Button(ventana, text="Abrir", width=12, command=abrir_archivo)
btn_abrir.grid(row=2, column=1)
    
btn_limpiar = tk.Button(ventana, text="Limpiar", width=12, command=limpiar_archivo)
btn_limpiar.grid(row=3, coLumn=1)

# Ejecutar aplicación 
ventana. mainloop()