import tkinter as tk
from tkinter import scrolledtext

# Clase Lexema
class Lexema:
    def __init__(self, tipo, valor, descripcion):
        self.tipo = tipo
        self.valor = valor
        self.descripcion = descripcion

    def __repr__(self):
        return f"Lexema({self.tipo}, '{self.valor}', '{self.descripcion}')"

# Función del analizador léxico
def analizador_lexico(cadena):
    cadena += "$"
    lexico = []
    contador_chars = 0

    while contador_chars < len(cadena):
        aux_palabra = ""
        uso_punto_decimal = False
        cha = cadena[contador_chars]

        if cha.isalpha():  # Palabras reservadas o identificadores
            while cadena[contador_chars].isalpha() or cadena[contador_chars].isdigit():
                if cadena[contador_chars] == ' ':
                    break
                aux_palabra += cadena[contador_chars]
                contador_chars += 1
                if contador_chars == len(cadena):
                    break

            if aux_palabra in ["if", "while", "return", "else", "int", "float", "void"]:
                lexico.append(Lexema(9, aux_palabra, f"palabra reservada {aux_palabra}"))
            else:
                lexico.append(Lexema(1, aux_palabra, "identificador"))

        elif cha.isdigit():  # Números y constantes
            while cadena[contador_chars].isdigit() or cadena[contador_chars] == '.':
                if cadena[contador_chars] == '.':
                    uso_punto_decimal = True
                aux_palabra += cadena[contador_chars]
                contador_chars += 1
                if contador_chars == len(cadena):
                    break

            if uso_punto_decimal:
                lexico.append(Lexema(13, aux_palabra, "número decimal"))
            else:
                lexico.append(Lexema(13, aux_palabra, "número entero"))

        elif cha in ['+', '-']:  # Operadores aritméticos
            aux_palabra += cha
            contador_chars += 1
            lexico.append(Lexema(14, aux_palabra, "operador aritmético"))

        elif cha == '|' and cadena[contador_chars + 1] == '|':  # Operador lógico OR
            aux_palabra = "||"
            contador_chars += 2
            lexico.append(Lexema(15, aux_palabra, "operador lógico OR"))

        elif cha == '&' and cadena[contador_chars + 1] == '&':  # Operador lógico AND
            aux_palabra = "&&"
            contador_chars += 2
            lexico.append(Lexema(15, aux_palabra, "operador lógico AND"))

        elif cha in ['*', '/']:  # Operadores aritméticos
            aux_palabra += cha
            contador_chars += 1
            lexico.append(Lexema(16, aux_palabra, "operador aritmético"))

        elif (cha == '=' and cadena[contador_chars + 1] == '=') or (cha == '!' and cadena[contador_chars + 1] == '='):  # Operadores lógicos
            aux_palabra = cha + cadena[contador_chars + 1]
            contador_chars += 2
            lexico.append(Lexema(17, aux_palabra, "operador lógico"))

        elif cha in ['<', '>']:  # Operadores relacionales
            aux_palabra += cha
            contador_chars += 1
            lexico.append(Lexema(17, aux_palabra, "operador relacional"))

        elif cha == '$':  # Fin de cadena
            aux_palabra += cha
            contador_chars += 1
            lexico.append(Lexema(18, aux_palabra, "fin de cadena"))

        elif cha.isspace():  # Ignorar espacios
            contador_chars += 1
            continue

        else:
            contador_chars += 1
            continue

    return lexico

# Función para el botón "Analizar"
def analizar():
    cadena = text_input.get("1.0", tk.END).strip()  # Obtener el texto del usuario
    lexico = analizador_lexico(cadena)  # Analizar la cadena
    text_output.delete("1.0", tk.END)  # Limpiar el área de salida
    for lexema in lexico:
        text_output.insert(tk.END, f"{lexema}\n")  # Mostrar cada lexema encontrado

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico de Tokens")

# Entrada de texto para ingresar los tokens
label_input = tk.Label(root, text="Ingrese los tokens o cadena de caracteres:")
label_input.pack()

text_input = scrolledtext.ScrolledText(root, height=5)
text_input.pack()

# Botón para iniciar el análisis
button_analizar = tk.Button(root, text="Analizar", command=analizar)
button_analizar.pack()

# Área de texto para mostrar el resultado del análisis
label_output = tk.Label(root, text="Resultado del análisis:")
label_output.pack()

text_output = scrolledtext.ScrolledText(root, height=10)
text_output.pack()

# Ejecutar la aplicación
root.mainloop()
