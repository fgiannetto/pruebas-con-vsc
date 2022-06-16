"""
LLEGUE HASTA EL VIDEO 130 DE LA SECCION 21
"""
from tkinter import*

ventana = Tk()
ventana.title("Marcos ! BEBECITA BEBELIN")
ventana.geometry("700x800")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="pink",
    bd=15,
    relief=RAISED
    )

marco.pack(side=RIGHT, anchor=S)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="pink",
    bd=15,
    relief=RAISED
    )

marco.pack(side=LEFT, anchor=S)

marco = Frame(ventana, width=200, height=650)
marco.config(
    bg="red",
    bd=15,
    relief=RAISED
    )

marco.pack(side=BOTTOM)

marco_PAPI = Frame(ventana, width=400, height=150)
marco_PAPI.config(
    bg="red",
    bd=15,
    relief=SOLID
    )

marco_PAPI.pack(side=TOP, fill=X)


ventana.mainloop()
