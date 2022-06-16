
def HolaMundo (nombre):
    return f"Hola {nombre} sos un salame"

def calculadora (num1, num2, basicas = False):
    suma = num1 + num2
    resta= num1 - num2
    multi= num2*num1
    div= num1/num2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: "  + str(multi)
    cadena += "\n"
    cadena += "Division: "  + str(div)
    cadena += "\n"

    return cadena 

