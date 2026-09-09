import random

print("Jogo de Adivinhação")
print(" Tente adivinhar o número que estou pensando entre 1 e 100")
print("Voce tem 7 tentativas para acertar o numero secreto")

numero_secreto = random.randint(1,100)

contador = 7
acertou = False 

while contador > 0:
    print(f'Voce tem {contador} tentativas restantes.')
    contador -= 1
    tentativa = int(input("Digite o seu palpite: "))
    if tentativa == numero_secreto:
       print("Parabens! Voce acertou!")
       acertou = True
       break 
    elif tentativa < numero_secreto:
       print("O numero secreto é maior que seu palpite")
    else:
       print("O numero secreto é menor que seu palpite")
       
if not acertou:
   print("Voce perdeu! O numero secreto era: ", numero_secreto)
else:
   print("Voce acertou o numero secreto em", 7 - contador + 1, "tentativas")