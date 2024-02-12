import random
import sys

print ("Bienvenido al juego de Blackjack. \n")

print ("¿Cómo jugar?:\n")

print ("En el juego de Blackjack, el jugador se enfrentará a la casa (en este caso la computadora). Para ganar, el jugador deberá obtener un número mayor que la casa, sin pasarse de 21. Si el jugador se pasa de 21 perderá automáticamente.\n")

print ("En total el juego maneja 13 cartas:\n")      
print ("Números de 2 al 10: Equivalen a su valor nominal.\n")
print ("Las letras J, Q, K: Valen 10 cada una.\n")
print ("AS: Puede valer 1 o 11, depende de tu elección y el juego que tengas.\n")}

inicio = int(input("Digita el número 1 para iniciar el juego. "))
formas=["Corazón","Trebol","Diamante","Pica"]
num=["A","J","K","Q"]+[(i)for i in range(2,11)]
mazo = [(p,v) for v in formas for p in num]

if inicio == 1:
  print("\nEl juego ha comenzado, la casa te dará dos cartas. ")

jugador=[]
def carj():
  a=len(mazo)-1
  nr=random.randint(0,a)
  jugador.append(mazo[nr])
  del mazo[nr]
for i in range(2):
  carj()
dealer=[]
def card():
  a=len(mazo)-1
  r=random.randint(0,a)
  dealer.append(mazo[r])
  del mazo[r]
for i in range(2):
  card()    
print("\nLa carta visible del crupier es: ")
print(dealer[0][0]," ",dealer[0][1])
print("\nTus cartas son:")
for i in range(len(jugador)):
    for j in range(len(jugador)):
        print(jugador[i][j]," ",end="")
    print("")
pjugador=0
for i in range(len(jugador)):
  if type(jugador[i][0])==int:
    pjugador+=jugador[i][0]
  elif type(jugador[i][0])==str:
    if jugador[i][0]=="A":
      pjugador+=11
    else:
      pjugador+=10
if pjugador==21:
  print("¡WOW! Es BlackJack.")
def opci():
  print("\nOpciones. ")
  print("1. Pedir otra carta.")
  print("2. Plantarse.")
  print("3. Rendirse.")
  n=int(input("Elige una opción:  "))
  return n

if pjugador!=21:
  n=opci()
  while(n!=2):
    if(n==1):
      carj()
      print("\nTus cartas son:")
      for i in range(len(jugador)):
          for j in range(2):
              print(jugador[i][j]," ",end="")
          print("")
      pjugador=0
      for i in range(len(jugador)):
        if type(jugador[i][0])==int:
          pjugador+=jugador[i][0]
        elif type(jugador[i][0])==str:
          if jugador[i][0]=="A":
            pjugador+=11
          else:
            pjugador+=10
      if pjugador>21:
        for i in range(len(jugador)):
          if jugador[i][0]=="A":
            pjugador-=10
          else:
            print("\nTe pasaste de 21, perdiste.")
            print("\nLas cartas crupier son:")
            for i in range(len(dealer)):
                for j in range(2):
                    print(dealer[i][j]," ",end="")
                print("")
            print("\nVictoria para el crupier.")
            print("\nGracias por jugar.")
            sys.exit()
      n=opci()
    elif(n==3):
      print("\nVictoria para el crupier.")
      sys.exit()
pdealer=0
for i in range(len(dealer)):
  if type(dealer[i][0])=="int":
    pdealer+=dealer[i][0]
  elif type(dealer[i][0])=="str":
    if dealer[i][0]=="A":
      pdealer+=11
    else:
      pdealer+=10
print("\nLas cartas del crupier son:")
for i in range(len(dealer)):
    for j in range(2):
        print(dealer[i][j]," ",end="")
    print("")
if pdealer<17:
  while (pdealer<=17):
    pdealer=0
    card()
    for i in range(len(dealer)):
      if type(dealer[i][0])==int:
        pdealer+=dealer[i][0]
      elif type(dealer[i][0])==str:
        if dealer[i][0]=="A":
          pdealer+=11
        else:
          pdealer+=10
    if pdealer>21:
      for i in range(len(dealer)):
        if dealer[i][0]=="A":
          pdealer-=10
        else:
          print ("\nEl crupier se pasó de 21, ¡ganaste!")
          sys.exit()
          
  print("\nLas cartas del crupier son:")
  for i in range(len(dealer)):
    for j in range(2):
        print(dealer[i][j]," ",end="")
    print("")
    

if pjugador > pdealer and pjugador<=21:
  print("\n¡Ganaste!")
elif pdealer > pjugador and pdealer<=21: 
  print("\nPerdiste. Victoria para el crupier.")