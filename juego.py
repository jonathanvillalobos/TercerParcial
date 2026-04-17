import tkinter as tk
import random

# Configuración inicial
numero_secreto = random.randint(1, 100)
vidas = 7

def verificar():
    global vidas
    
    try:
        intento = int(entrada.get())
        
        if intento < 1 or intento > 100:
            resultado.set("⚠️ Número entre 1 y 100")
            return
        
        if intento < numero_secreto:
            vidas -= 1
            resultado.set(f"🔼 Muy bajo | Vidas: {vidas}")
        elif intento > numero_secreto:
            vidas -= 1
            resultado.set(f"🔽 Muy alto | Vidas: {vidas}")
        else:
            resultado.set("🎉 ¡Ganaste!")
            boton.config(state="disabled")
        
        if vidas == 0:
            resultado.set(f"💀 Perdiste. Era {numero_secreto}")
            boton.config(state="disabled")
    
    except:
        resultado.set("⚠️ Ingresa un número válido")

def reiniciar():
    global numero_secreto, vidas
    numero_secreto = random.randint(1, 100)
    vidas = 7
    resultado.set("Nuevo juego 🎮")
    entrada.delete(0, tk.END)
    boton.config(state="normal")

# Ventana
ventana = tk.Tk()
ventana.title("Adivina el número PRO")
ventana.geometry("350x250")

# Widgets
tk.Label(ventana, text="🎮 Adivina el número (1-100)", font=("Arial", 14)).pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Intentar", command=verificar)
boton.pack(pady=5)

tk.Button(ventana, text="Reiniciar", command=reiniciar).pack(pady=5)

resultado = tk.StringVar()
resultado.set("Tienes 7 vidas ❤️")

tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack(pady=10)

ventana.mainloop()