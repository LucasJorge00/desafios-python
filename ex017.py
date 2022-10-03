# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

catOposto = float(input("Comprimento do cateto oposto: "))
catAdjacente = float(input("Comprimento do cateto adjacente: "))
hip = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hip))