import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

#se crea la ventana principal
ventana = tk.Tk()
ventana.title("Máquina Expendedora")
ventana.geometry("450x400")

#diccionario que guarda cuántos refrescos hay de cada tipo
inventario = {
    "Coca": 5,
    "Fanta": 5,
    "Sprite": 5,
    "Mundet": 5
}

#precio de cada refresco y dinero ingresado por el usuario
precio = 5
dinero = 0

#variable que guarda la opción seleccionada en los radiobuttons
opcion = tk.StringVar()

#función que suma el dinero insertado
def insertar_moneda(valor):
    global dinero  #permite modificar la variable global
    dinero += valor
    label_dinero.config(text=f"$ {dinero}")  #actualiza el texto en pantalla
    habilitar_radios()  #activa o desactiva opciones

#función para validar el dinero que se ingresa manualmente
def ingresar_dinero():
    try:
        valor = float(entrada_dinero.get())  #convierte el texto a número
        if valor in [0.5, 1, 2, 5, 10]:  #solo acepta estas monedas
            insertar_moneda(valor)
        else:
            messagebox.showerror("Error", "Moneda no válida")
    except:
        messagebox.showerror("Error", "Ingresa un número válido")

#activa o desactiva los radiobuttons según dinero y stock
def habilitar_radios():
    for rb in radios:
        nombre = rb.cget("value")  #obtiene el nombre del refresco
        if dinero >= precio and inventario[nombre] > 0:
            rb.config(state="normal")  #se puede seleccionar
        else:
            rb.config(state="disabled")  #no disponible

#ventana que aparece después de comprar
def ventana_compra(producto, cambio):
    top = tk.Toplevel(ventana)  #crea una nueva ventana
    top.title("Compra realizada")
    top.geometry("300x300")

    tk.Label(top, text="GRACIAS POR SU COMPRA", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(top, text=f"Su cambio es: $ {cambio}").pack(pady=5)

    try:
        #elige la ruta de la imagen dependiendo del producto
        if producto == "Coca":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/coca.png"
        elif producto == "Fanta":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/fanta.png"
        elif producto == "Sprite":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/sprite.png"
        elif producto == "Mundet":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/mundet.png"
        else:
            ruta = ""

        if ruta != "":
            img = Image.open(ruta)  #abre la imagen
            img = img.resize((120, 120))  #cambia tamaño
            img_tk = ImageTk.PhotoImage(img)  #la convierte para tkinter

            label = tk.Label(top, image=img_tk)
            label.image = img_tk  #evita que se borre la imagen
            label.pack(pady=10)

    except:
        tk.Label(top, text="Error al cargar imagen").pack()

    tk.Button(top, text="OK", command=top.destroy).pack(pady=10)

#función que realiza la compra
def tomar_refresco():
    global dinero
    
    seleccion = opcion.get()  #obtiene el refresco seleccionado

    if seleccion == "":
        messagebox.showerror("Error", "Selecciona un refresco")
        return

    #verifica que haya producto y dinero suficiente
    if inventario[seleccion] > 0 and dinero >= precio:
        inventario[seleccion] -= 1  #reduce el stock

        cambio = dinero - precio  #calcula el cambio
        dinero = 0  #reinicia el dinero

        label_dinero.config(text=f"$ {dinero}")
        label_cambio.config(text=f"Cambio: $ {cambio}")

        actualizar_texto()  #actualiza cantidades
        opcion.set("")  #limpia selección
        label_imagen.config(image="")  #quita imagen

        ventana_compra(seleccion, cambio)  #abre ventana final
        habilitar_radios()

    else:
        messagebox.showerror("Error", "Sin stock o dinero insuficiente")

#actualiza texto de los radiobuttons
def actualizar_texto():
    radio_coca.config(text=f"Coca   {inventario['Coca']}")
    radio_fanta.config(text=f"Fanta  {inventario['Fanta']}")
    radio_sprite.config(text=f"Sprite {inventario['Sprite']}")
    radio_mundet.config(text=f"Mundet {inventario['Mundet']}")

    #desactiva si ya no hay producto
    radio_coca.config(state="disabled" if inventario["Coca"] == 0 else "normal")
    radio_fanta.config(state="disabled" if inventario["Fanta"] == 0 else "normal")
    radio_sprite.config(state="disabled" if inventario["Sprite"] == 0 else "normal")
    radio_mundet.config(state="disabled" if inventario["Mundet"] == 0 else "normal")

#muestra la imagen del refresco seleccionado
def mostrar_imagen():
    seleccion = opcion.get()

    if seleccion == "":
        return

    try:
        #elige la ruta según la selección
        if seleccion == "Coca":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/coca.png"
        elif seleccion == "Fanta":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/fanta.png"
        elif seleccion == "Sprite":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/sprite.png"
        elif seleccion == "Mundet":
            ruta = "C:/Users/Jonny/programacion1/tercerParcial/maquina_expendedora/mundet.png"
        else:
            ruta = ""

        if ruta != "":
            img = Image.open(ruta)
            img = img.resize((120, 120))
            img_tk = ImageTk.PhotoImage(img)

            label_imagen.config(image=img_tk)
            label_imagen.image = img_tk  #importante para que no desaparezca

    except:
        label_imagen.config(image="")

#ventana para agregar más productos
def ventana_surtir(refresco):
    top = tk.Toplevel(ventana)
    top.title(f"Surtir {refresco}")
    top.geometry("250x150")

    tk.Label(top, text=f"Ingrese cantidad de {refresco}:").pack(pady=10)
    
    entrada = tk.Entry(top)
    entrada.pack()

    def confirmar():
        try:
            cantidad = int(entrada.get())
            if cantidad >= 0:
                inventario[refresco] += cantidad  #aumenta stock
                actualizar_texto()
                habilitar_radios()
                messagebox.showinfo("OK", f"{refresco}: {inventario[refresco]} en existencia")
                top.destroy()
            else:
                messagebox.showerror("Error", "No negativos")
        except:
            messagebox.showerror("Error", "Ingresa un número válido")

    tk.Button(top, text="Aceptar", command=confirmar).pack(pady=10)

#ventana para cambiar el precio
def ventana_precio():
    global precio

    top = tk.Toplevel(ventana)
    top.title("Cambiar precio")
    top.geometry("250x150")

    tk.Label(top, text="Nuevo precio:").pack(pady=10)
    
    entrada = tk.Entry(top)
    entrada.pack()

    def confirmar():
        global precio
        try:
            nuevo = float(entrada.get())
            
            if nuevo >= 0:
                precio = nuevo  #cambia el precio
                label_precio.config(text=f"Precio: $ {precio}")
                habilitar_radios()
                messagebox.showinfo("OK", f"Nuevo precio: ${precio}")
                top.destroy()
            else:
                messagebox.showerror("Error", "No negativos")
        except:
            messagebox.showerror("Error", "Valor inválido")

    tk.Button(top, text="Aceptar", command=confirmar).pack(pady=10)

#creación del menú superior
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_surtir = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Surtir", menu=menu_surtir)

#opciones del menú para surtir cada refresco
menu_surtir.add_command(label="Coca", command=lambda: ventana_surtir("Coca"))
menu_surtir.add_command(label="Fanta", command=lambda: ventana_surtir("Fanta"))
menu_surtir.add_command(label="Sprite", command=lambda: ventana_surtir("Sprite"))
menu_surtir.add_command(label="Mundet", command=lambda: ventana_surtir("Mundet"))

barra_menu.add_command(label="Cambiar Precio", command=ventana_precio)

#interfaz principal
tk.Label(ventana, text="0.5, 1, 2, 5, 10").grid(row=0, column=0)

entrada_dinero = tk.Entry(ventana, width=10)
entrada_dinero.grid(row=0, column=1)

label_dinero = tk.Label(ventana, text="$ 0.0")
label_dinero.grid(row=0, column=2)

tk.Button(ventana, text="Ingresar", command=ingresar_dinero).grid(row=1, column=0, columnspan=2)

label_precio = tk.Label(ventana, text=f"Precio: $ {precio}")
label_precio.grid(row=1, column=2)

label_cambio = tk.Label(ventana, text="Cambio: $ 0.0")
label_cambio.grid(row=2, column=1, columnspan=2)

frame_main = tk.LabelFrame(ventana, text="Refrescos")
frame_main.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

frame_izq = tk.Frame(frame_main)
frame_izq.grid(row=0, column=0)

#botones de selección de refrescos
radio_coca = tk.Radiobutton(frame_izq, text="Coca 5", variable=opcion, value="Coca", state="disabled", command=mostrar_imagen)
radio_coca.grid(row=0, column=0, sticky="w")

radio_fanta = tk.Radiobutton(frame_izq, text="Fanta 5", variable=opcion, value="Fanta", state="disabled", command=mostrar_imagen)
radio_fanta.grid(row=1, column=0, sticky="w")

radio_sprite = tk.Radiobutton(frame_izq, text="Sprite 5", variable=opcion, value="Sprite", state="disabled", command=mostrar_imagen)
radio_sprite.grid(row=2, column=0, sticky="w")

radio_mundet = tk.Radiobutton(frame_izq, text="Mundet 5", variable=opcion, value="Mundet", state="disabled", command=mostrar_imagen)
radio_mundet.grid(row=3, column=0, sticky="w")

radios = [radio_coca, radio_fanta, radio_sprite, radio_mundet]

#zona donde se muestra la imagen
frame_der = tk.Frame(frame_main, width=150, height=150, bd=1, relief="solid")
frame_der.grid(row=0, column=1, padx=20)

label_imagen = tk.Label(frame_der)
label_imagen.pack()

#botón para comprar
tk.Button(ventana, text="Tomar Refresco", command=tomar_refresco).grid(row=4, column=0, columnspan=3, pady=10)

ventana.mainloop()