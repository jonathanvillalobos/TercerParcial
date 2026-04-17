import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date

# Ventana
ventana = tk.Tk()
ventana.title("Signo Zodiacal Chino")
ventana.geometry("700x400")

# -------- FRAME IZQUIERDO --------
frame_izq = tk.Frame(ventana, bg="white", bd=2, relief="solid")
frame_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

tk.Label(frame_izq, text="Datos Personales",
         bg="white", font=("Arial", 14, "bold")).pack(pady=10)

# Nombre
tk.Label(frame_izq, text="Nombre", bg="white").pack(anchor="w", padx=10)
entrada_nombre = tk.Entry(frame_izq)
entrada_nombre.pack(padx=10, pady=3, fill="x")

# Apellido paterno
tk.Label(frame_izq, text="Apaterno", bg="white").pack(anchor="w", padx=10)
entrada_paterno = tk.Entry(frame_izq)
entrada_paterno.pack(padx=10, pady=3, fill="x")

# Apellido materno
tk.Label(frame_izq, text="Amaterno", bg="white").pack(anchor="w", padx=10)
entrada_materno = tk.Entry(frame_izq)
entrada_materno.pack(padx=10, pady=3, fill="x")

# Fecha
tk.Label(frame_izq, text="Fecha de nacimiento",
         bg="white").pack(pady=10)

frame_fecha = tk.Frame(frame_izq, bg="white")
frame_fecha.pack()

entrada_dia = tk.Entry(frame_fecha, width=5)
entrada_dia.grid(row=0, column=0, padx=5)
tk.Label(frame_fecha, text="Día", bg="white").grid(row=1, column=0)

entrada_mes = tk.Entry(frame_fecha, width=5)
entrada_mes.grid(row=0, column=1, padx=5)
tk.Label(frame_fecha, text="Mes", bg="white").grid(row=1, column=1)

entrada_anio = tk.Entry(frame_fecha, width=8)
entrada_anio.grid(row=0, column=2, padx=5)
tk.Label(frame_fecha, text="Año", bg="white").grid(row=1, column=2)

# Sexo
tk.Label(frame_izq, text="Sexo", bg="white").pack(pady=10)

sexo = tk.StringVar()

tk.Radiobutton(frame_izq, text="Masculino", variable=sexo,
               value="Masculino", bg="white").pack(anchor="w", padx=20)
tk.Radiobutton(frame_izq, text="Femenino", variable=sexo,
               value="Femenino", bg="white").pack(anchor="w", padx=20)

# LÍNEA DIVISORIA
linea = tk.Frame(ventana, bg="black", width=2)
linea.pack(side="left", fill="y")

# FRAME DERECHO 
frame_der = tk.Frame(ventana, bg="white")
frame_der.pack(side="right", fill="both", padx=10, pady=10)

label_resultado = tk.Label(frame_der, text="",
                          bg="white", font=("Arial", 14))
label_resultado.pack(pady=20)

label_imagen = tk.Label(frame_der, bg="white")
label_imagen.pack(pady=10)


imagenes = {
    "Rata": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\rata.png").resize((120,120))),
    "Buey": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\buey.png").resize((120,120))),
    "Tigre": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\tigre.png").resize((120,120))),
    "Conejo": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\conejo.png").resize((120,120))),
    "Dragon": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\dragon.png").resize((120,120))),
    "Serpiente": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\serpiente.png").resize((120,120))),
    "Caballo": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\caballo.png").resize((120,120))),
    "Cabra": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\cabra.png").resize((120,120))),
    "Mono": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\mono.png").resize((120,120))),
    "Gallo": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\gallo.png").resize((120,120))),
    "Perro": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\perro.png").resize((120,120))),
    "Cerdo": ImageTk.PhotoImage(Image.open(r"C:\Users\Jonny\programacion1\tercerParcial\Zodiaco chino\cerdo.png").resize((120,120)))
}

# Función
def calcular():
    try:
        nombre = entrada_nombre.get()
        paterno = entrada_paterno.get()
        materno = entrada_materno.get()
        ano = int(entrada_anio.get())
        mes = int(entrada_mes.get())
        dia = int(entrada_dia.get())

        if nombre == "" or paterno == "" or materno == "":
            messagebox.showerror("Error", "Completa todos los datos")
            return
        
        signos = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey",
                  "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"]

        signo = signos[ano % 12]
        dia_actual = 27
        mes_actual = 3
        anio_actual = 2026

        edad = anio_actual - ano

        if (mes_actual, dia_actual) < (mes, dia):
            edad -= 1
        # ----------------------------------

        label_resultado.config(
            text=f"Hola {nombre} {paterno} {materno}\n"
                 f"Tienes {edad} años\n"
                 f"Tu signo zodiacal es:\n{signo}"
        )
        label_imagen.config(image=imagenes[signo])
        label_imagen.image = imagenes[signo]
    except:
        messagebox.showerror("Error", "Datos inválidos")


btn = tk.Button(frame_izq, text="Imprimir",
                command=calcular,
                bg="black", fg="white",
                font=("Arial", 12))
btn.pack(pady=15)

ventana.mainloop()