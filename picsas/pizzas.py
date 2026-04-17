import customtkinter
import tkinter as tk
from tkinter import ttk, messagebox

# CONFIGURACIÓN 
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# PRECIOS 
precios = {
    "Chica": 50,
    "Mediana": 80,
    "Grande": 120
}

# VENTANA 
ventana = customtkinter.CTk()
ventana.title("Pizzería")
ventana.geometry("900x500")  # un poco más ancho para que quepa todo

# VARIABLES 
nombre = tk.StringVar()
direccion = tk.StringVar()
telefono = tk.StringVar()
fecha = tk.StringVar()

tamano = tk.StringVar(value="Chica")
cantidad = tk.IntVar(value=1)

# VARIABLES DE INGREDIENTES
jamon = tk.BooleanVar()
pina = tk.BooleanVar()
champi = tk.BooleanVar()

# FUNCIONES
def agregar():
    t = tamano.get()
    cant = cantidad.get()
    nom = nombre.get()

    # OBTENER INGREDIENTES
    lista_ing = []
    if jamon.get():
        lista_ing.append("Jamón")
    if pina.get():
        lista_ing.append("Piña")
    if champi.get():
        lista_ing.append("Champiñones")

    ing = ", ".join(lista_ing)

    # VALIDAR INGREDIENTES
    if ing == "":
        messagebox.showerror("Error", "Selecciona al menos un ingrediente")
        return

    # VALIDAR NOMBRE
    if nom == "":
        messagebox.showerror("Error", "Ingresa el nombre del cliente")
        return

    # CALCULAR SUBTOTAL
    subtotal = precios[t] * cant

    # AGREGAR A TABLA PRINCIPAL
    tabla.insert("", "end", values=(nom, t, ing, cant, subtotal))

    # AGREGAR A TABLA DEL DÍA
    tabla_dia.insert("", "end", values=(nom, t, ing, cant, subtotal))

    # GUARDAR EN ARCHIVO
    with open("C:/Users/Jonny/programacion1/tercerParcial/picsas/pedidos.txt", "a") as f:
        f.write(f"{nom},{t},{ing},{cant},{subtotal}\n")


def quitar():
    seleccionado = tabla.selection()

    if seleccionado:
        tabla.delete(seleccionado)
    else:
        messagebox.showwarning("Aviso", "Selecciona un producto")


def terminar():
    total = 0

    # CALCULAR TOTAL DESDE TABLA
    for item in tabla.get_children():
        valores = tabla.item(item, "values")
        total += int(valores[4])

    messagebox.showinfo("Total", f"Total a pagar: ${total}")

    # LIMPIAR TABLA PRINCIPAL
    for item in tabla.get_children():
        tabla.delete(item)


# APARTADO DE CLIENTE 
frame_cliente = customtkinter.CTkFrame(ventana)
frame_cliente.pack(pady=10, padx=10, fill="x")

customtkinter.CTkLabel(frame_cliente, text="Nombre").grid(row=0, column=0)
customtkinter.CTkEntry(frame_cliente, textvariable=nombre).grid(row=0, column=1)

customtkinter.CTkLabel(frame_cliente, text="Dirección").grid(row=1, column=0)
customtkinter.CTkEntry(frame_cliente, textvariable=direccion).grid(row=1, column=1)

customtkinter.CTkLabel(frame_cliente, text="Telefono").grid(row=2, column=0)
customtkinter.CTkEntry(frame_cliente, textvariable=telefono).grid(row=2, column=1)

customtkinter.CTkLabel(frame_cliente, text="Fecha").grid(row=3, column=0)
customtkinter.CTkEntry(frame_cliente, textvariable=fecha).grid(row=3, column=1)

# APARTADO DE PIZZA 
frame_pizza = customtkinter.CTkFrame(ventana)
frame_pizza.pack(pady=10, padx=10, fill="x")

customtkinter.CTkLabel(frame_pizza, text="Tamaño").grid(row=0, column=0, pady=10, padx=10)

customtkinter.CTkRadioButton(frame_pizza, text="Chica", variable=tamano, value="Chica").grid(row=0, column=1)
customtkinter.CTkRadioButton(frame_pizza, text="Mediana", variable=tamano, value="Mediana").grid(row=0, column=2)
customtkinter.CTkRadioButton(frame_pizza, text="Grande", variable=tamano, value="Grande").grid(row=0, column=3)

customtkinter.CTkLabel(frame_pizza, text="Ingredientes").grid(row=1, column=0)

customtkinter.CTkCheckBox(frame_pizza, text="Jamón", variable=jamon).grid(row=1, column=1)
customtkinter.CTkCheckBox(frame_pizza, text="Piña", variable=pina).grid(row=1, column=2)
customtkinter.CTkCheckBox(frame_pizza, text="Champiñones", variable=champi).grid(row=1, column=3)

customtkinter.CTkLabel(frame_pizza, text="Cantidad").grid(row=2, column=0)
customtkinter.CTkEntry(frame_pizza, textvariable=cantidad).grid(row=2, column=1)

# -------- FRAME PARA TABLAS --------
frame_tablas = customtkinter.CTkFrame(ventana)
frame_tablas.pack(pady=10, fill="both", expand=True)

# TABLA PRINCIPAL (IZQUIERDA)
tabla = ttk.Treeview(frame_tablas, columns=("Nombre","Tamano", "Ingredientes", "Cantidad", "Subtotal"), show="headings")

tabla.heading("Nombre", text="Nombre")
tabla.heading("Tamano", text="Tamano")
tabla.heading("Ingredientes", text="Ingredientes")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Subtotal", text="Subtotal")

tabla.pack(side="left", padx=10, fill="both", expand=True)

# -------- TABLA DERECHA (PEDIDOS DEL DÍA) --------
frame_derecho = customtkinter.CTkFrame(frame_tablas)
frame_derecho.pack(side="right", padx=10, fill="both")

customtkinter.CTkLabel(frame_derecho, text="Pedidos del día").pack(pady=5)

tabla_dia = ttk.Treeview(frame_derecho, columns=("Nombre","Tamano","Ingredientes","Cantidad","Subtotal"), show="headings")

tabla_dia.heading("Nombre", text="Nombre")
tabla_dia.heading("Tamano", text="Tamano")
tabla_dia.heading("Ingredientes", text="Ingredientes")
tabla_dia.heading("Cantidad", text="Cantidad")
tabla_dia.heading("Subtotal", text="Subtotal")

tabla_dia.pack(fill="x")

# BOTONES 
frame_botones = customtkinter.CTkFrame(ventana)
frame_botones.pack(pady=10)

customtkinter.CTkButton(frame_botones, text="Agregar", command=agregar).grid(row=0, column=0, padx=5)
customtkinter.CTkButton(frame_botones, text="Quitar", command=quitar).grid(row=0, column=1, padx=5)
customtkinter.CTkButton(frame_botones, text="Terminar", command=terminar).grid(row=0, column=2, padx=5)

ventana.mainloop()