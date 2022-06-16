from tkinter import* 

ventana = Tk()
#ventana.geometry("500x500")



texto = Label(ventana, text = "Bienvenido al programitahh")
texto.config(
    fg="white",
    bg="black",
    padx = 20,
    pady = 20,
    font=("Arial", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text = "Básico")
texto.config(
    #width = 500,
    height = 9,
    bg="orange",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text = "Hola perrrriiii (1)")
texto.config(
    #width = 500,
    height = 4,
    bg="red",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = "Hola perrrriiii (2)")
texto.config(
    #width = 500,
    height = 3,
    bg="brown",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)

texto = Label(ventana, text = "Hola perrrriiii")
texto.config(
    #width = 500,
    height = 5,
    bg="blue",
    font=("Times New Roman", 15),
    cursor="spider"
)
texto.pack(side=RIGHT, fill=X, expand=YES)


ventana.mainloop()