print("\n-------------------------------------------------------------------------------")
#Exercicio 1

print("Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.\n")

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)
print("\n-------------------------------------------------------------------------------")
#Exercicio 2

print("\nExercício 2 - Crie uma lista de 5 objetos e imprima na tela\n")

coisas= ["Carro", "Banana", "Carteira", "Chiclete", "Para-Raios"]
print (coisas)
print("\n-------------------------------------------------------------------------------")
#Exercicio 3

print("\nExercício 3 - Crie duas strings e concatene as duas em uma terceira string\n")

x="Celta"
y="Cromado"
xy = x + " " + y
print(xy)
print("\n-------------------------------------------------------------------------------")
#Exercicio 4

print ("\nExercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla\n")

tupla = (1, 2, 3, 4, 4, 4, 5)
contagem = tupla.index(4)
print("Essa Tupla possui",len(tupla), "Items")
print("Essa tupla contém",contagem, "Numeros 4")
print("\n-------------------------------------------------------------------------------")
#Exercicio 5

print("\nExercício 5 - Crie um dicionário vazio e imprima na tela\n")

dict = {}
print(dict)
print("\n-------------------------------------------------------------------------------")
#Exercicio 6

print("\nExercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela\n")

dicionario = {"cor":"Vermelha", "fruta":"Banana", "chocolate":"Milka"}
print(dicionario)

print("\n-------------------------------------------------------------------------------")
#Exercicio 7

print("\nExercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela\n")

dicionario["jogo"] = "FF XV"
print(dicionario)

print("\n-------------------------------------------------------------------------------")
#Exercicio 8

print("\nExercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.\n Imprima o dicionário na tela.\n")

dicionario["sorte"] = 2, 7
print(dicionario)

print("\n-------------------------------------------------------------------------------")
#Exercicio 9

print("\nExercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string") 
print("o segundo uma tupla de 2 elementos,\n o terceiro um dcionário com 2 chaves e 2 valores\n e o quarto elemento um valor do tipo float. Imprima a lista na tela.\n")

list1 = ["Banana",tuple(("Jorge","Cariani")) , {"Carros": "Volvo","Chocolate": "Milka"}, 4.0]

print(list1)

print("\n-------------------------------------------------------------------------------")

#Exercicio 10

print("\nExercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.\n")
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])

print("\n-------------------------------------------------------------------------------")