# Escreva o número de palavras de um texto.

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

texto = texto + " "

contador = 0

esp = texto.find(" ")
while esp != -1:
    contador = contador + 1

    texto = texto[esp + 1:len(texto)]

    esp = texto.find(" ")

print("O texto tem", contador, "palavras.")
