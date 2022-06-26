# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#Author: Luiz Marques
#Create Date: 20220626
#Programa sem muito tratamento de erro de entrada. Programa simples.
#Jogo que simula um dado.
import random
cont=0
controle=""
resposta=input("Você que jogar um jogo de dado? SIM|NAO\n").upper()
if resposta == "SIM":
    while controle != "S":
            cont = cont + 1
            x = random.randrange(1,6)
            print("Número sorteado: ", x, "Número de jogadas: ",cont)
            resposta=input("Deseja jogar dado novamente? SIM|NAO\n").upper()
            if resposta == "SIM":
                controle = "N"
            else:
                print("Bye bye!")
                controle = "S"
else:
    print("Então tudo bem, até mais!")
print("Fim do progama!")