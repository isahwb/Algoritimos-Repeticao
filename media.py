#Leia 5 números e calcule média.

media=0
for i in range(1,6):
    numero= int(input("Digite um número: " ))
    media += numero
media =  media/ 5 
print(f"A média é: {media}")