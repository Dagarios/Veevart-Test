#Importamos los packetes necesarios
import random
import time

def inicio():
    #Menu del juego
    print("\n\n\n")
    print ("================================")
    print ("     Serpientes y escaleras     ")
    print ("================================\n")

    print("   Bienvenido al juego")
    print("   Precione ENTER para comenzar la partida!\n")
    x = input("")
    Juego()

def Juego():
    #Aqui epieza el juego
    #Definimos variables
    StartEscaleras = [3,6,9,10]
    EndEscaleras = [11,17,18,12]
    EscaleraCounter = 0

    StartSerpiente = [14,19,22,24]
    EndSerpiente = [4,8,20,16]
    SerpienteCounter = 0

    Player = 1

    #Recorrido del juego
    while True:
        print("\n\n")
        print("La posicion actual es: ",Player)
        print("lanzando el dado")
        time.sleep(1.5)

        #Se lanza el dado del juego
        step = Dado()
        print("\nEl dado saco un ",step)

        #Avanzamos la posicion
        Player = Player+step
        time.sleep(1.5)

        #Verificamos si callo en una escalera
        for i in range(4):
            if(Player == StartEscaleras[i]):
                print("\nEncontraste una escalera!")
                Player = EndEscaleras[i]
                print("Y te llevo a la casilla ",Player)
                EscaleraCounter = EscaleraCounter+1
                time.sleep(1.5)

        #Verificamos si callo en una serpiente
        for i in range(4):
            if(Player == StartSerpiente[i]):
                print("\nCaiste en una serpiente!")
                Player = EndSerpiente[i]
                print("Y te llevo a la casilla ",Player)
                SerpienteCounter = SerpienteCounter+1
                time.sleep(1.5)

        #Verificamos si llego a la casilla final
        if (Player >= 25):
            #Mensaje final
            print("\nLlegaste a la casilla 25")
            print("\n=========================================\n")
            print("\n              Has ganado!!!                ")
            print("\n   Subiste",EscaleraCounter,"escaleras")
            print  ("   Caiste en",SerpienteCounter,"serpientes")
            print("\n=========================================\n")
            time.sleep(1.5)
            #Volvemos al menu
            x = input("Pulsa ENTER para volver al menu")
            inicio()

def Dado():
    #Dado del juego
    dado = random.randint(1,6)
    return dado

#Esto inicia el juego
inicio()