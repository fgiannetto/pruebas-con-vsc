from tkinter import* 

ventana = Tk()
ventana.geometry("500x500")

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text = "Bienvenido al programitahh")
texto.config(
    fg="white",
    bg="black",
    padx = 20,
    pady = 20,
    font=("Arial", 30)
)
texto.pack()

texto = Label(ventana, text = pruebas(pais="Fran", apellidos="Giann", nombre="ARG"))
texto.config(
    #width = 500,
    height = 15,
    bg="orange",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(anchor= E)
texto = Label(ventana, text = "Hola perrrriiii")
texto.config(
    #width = 500,
    height = 40,
    bg="red",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(anchor= NW)

ventana.mainloop()