#--------Proyecto Final Equipo 10 - Juego Didáctico-------------------
'''
Maria Fernanda Castañeda de la Rosa A01620882
'''
import time
#----------------------Funciones--------------------------------------
def bienvenida():    #Función para mostrar la bienvenida al usuario
    menu=0
    if eleccion == 0:
        while menu==0:        
            bienvenida = open("bienvenidareto.txt", "r")
            for n in bienvenida:
                print(n)
            time.sleep(1)
            menu = int(input("\nTeclea 1 y enter para salir al menú principal: "))
            if menu == "1":
                menu=1

def juego1():    #Función para correr el primer juego
    if eleccion == 1:
        print("\n--------------JUEGO 1------------------")
        juego1_ciclo = 1
        cor = 0
        inc = 0
        while (juego1_ciclo == 1):  #Ciclo para mantenerse jugando hasta que se desee salir
            import random
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)

            while (n1 == n2):
                n1 = random.randint(1,100)
                n2 = random.randint(1,100)
                
            print("\nNumero 1: ",n1,"\nNumero 2: ",n2)
            
            print("\nESCRIBE EL NUMERO MAS GRANDE: ",end=" ")
            num = int(input())
            
            if num != n1 and num != n2:
                print("Tu respuesta no entra en el juego, inténtalo de nuevo")
                inc+=1
            elif n1>n2:
                if num == n1:
                    cor+=1
                else:
                    inc+=1
            elif n2>n1:
                if num == n2:
                    cor+=1
                else:
                    inc+=1
            
            print("\nSi quieres jugar de nuevo apreta '1' y enter \nSi quieres dejar de jugar apreta '2' y enter \n¿Qué quieres hacer? ", end="")
            juego1_ciclo = int(input())
    

        totales = cor+inc
        print("\nIntentos TOTALES: ",totales)
        print("Intentos CORRECTOS: ",cor)
        print("Intentos INCORRECTOS",inc)

        texto = open("resultados.txt", "w") #Abrir archivo para escribir resultados
        texto.write("Intentos TOTALES: "+str(totales)+"\n")
        texto.write("Intentos CORRECTOS: "+str(cor)+"\n")
        texto.write("Intentos INCORRECTOS: "+str(inc))
        texto.close()
        time.sleep(1)

def juego2(): #Función para correr el segundo juego
    if eleccion == 2:
        juego2_ciclo = 1
        while (juego2_ciclo == 1):  #Ciclo para mantenerse jugando hasta que se desee salir
            print("\n--------------JUEGO 2------------------")
            jug1 = input("¿Cual es el nombre del primer jugador?: ")
            jug2 = input("¿Cual es el nombre del segundo jugador?: ")


            lista1 = ["1","2","3","4","5","6"]
            lista2 = ["1","2","3","4","5","6"]
            print("\nAhora se va a tirar el dado")

            sum_jug1 = 0
            sum_jug2 = 0
            for i in range(1,7):
                import random
                print ("\nEs el turno de", jug1)
                dado1=random.randint(1,6)
                print ("\nEl numero que te salió en el dado es" , dado1)
                print("Por cual de estos numeros ("," ".join(lista1),")lo quieres multiplicar?: ", end="")
                num1 = input()
                
                num_repe_j1 = 1
                while num_repe_j1 == 1:
                    if num1 not in lista1:
                        print("Ese numero no esta en la lista, dame otro numero\n")
                        print("Por cual de estos numeros ("," ".join(lista1),")lo quieres multiplicar?: ", end="")
                        num1 = input()
                    else:       
                        num_repe_j1 = 0
                        lista1.remove(num1)
                        rejug1=(i*dado1)
                        sum_jug1=sum_jug1+rejug1
                        
                print ("\nEs el turno de", jug2)
                dado2=random.randint(1,6)
                print ("\nEl numero que te salió en el dado es" , dado2)
                print("Por cual de estos numeros ("," ".join(lista2),")lo quieres multiplicar? ", end="")
                num2 = input()
                
                num_repe_j2 = 1
                while num_repe_j2 == 1: 
                    if num2 not in lista2:
                        print("Ese numero no esta en la lista, dame otro numero\n")
                        print("Por cual de estos numeros ("," ".join(lista2),")lo quieres multiplicar?: ", end="")
                        num2 = input()
                    else:
                        num_repe_j2 = 0
                        lista2.remove(num2)
                        rejug2=(i*dado2)
                        sum_jug2=sum_jug2+rejug2

            if sum_jug1 < sum_jug2:
                print(jug1,"obtuvo", sum_jug1, "pts y", jug2, "obtuvo", sum_jug2, "Entonces, el ganador es" , jug2,"\n")
            else:
                print(jug1,"obtuvo", sum_jug1, "pts y", jug2, "obtuvo", sum_jug2, "Entonces, el ganador es" , jug1,"\n")
                
            print("\nSi quieres jugar de nuevo apreta '1' y enter \nSi quieres dejar de jugar apreta '2' y enter \n¿Qué quieres hacer? ", end="")
            juego2_ciclo = int(input())
            
#------------------Programa principal---------------------------------
ciclo = 0 
while(ciclo == 0): #Ciclo para mantenerse en el menú hasta que el usuario quiera salir
    print("\nHola ¡Bienvenido!, ¿que quieres hacer? ")
    print("Si no sabes como jugar ve a la bienvenida\n")
    print("Para ir a la bienvenida teclea 0 y enter")
    print("Para ir al juego 1 teclea 1 y enter")
    print("Para ir al juego 2 teclea 2 y enter")
    print("Para salir teclea 3 y enter")
    
    eleccion = int(input("\n¿Qué quieres hacer?: "))
    time.sleep(1)
#---------------------BIENVENIDA--------------------------------------
    bienvenida()
#-----------------------JUEGO 1---------------------------------------                
    juego1()
#-----------------------JUEGO 2---------------------------------------
    juego2()
#-----------------------SALIDA----------------------------------------
    if eleccion == 3:
        ciclo = 1
        print("---------Gracias por jugar-----------")
