import customtkinter

def button_callback():
   print("button pressed")
   
app = customtkinter.CTk()
app.title("my app")
app.geometry ("428x158")
app.grid_columnconfigure((0), weight=1)

button = customtkinter.CkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=b, padx=20, pady=20, sticky="ew", columnspan=2) 
checkbox_1= customtkinter, CTkCheckBox (app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0,20), sticky="w")
checkbox_2= customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid (row=1, column=1, padx=20, pady=(0,20), sticky= "w")

app.mainloop()