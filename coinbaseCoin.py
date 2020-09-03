
#LIBRERIAS:
from coinbase.wallet.client import Client
import threading
import os
import math
import json
from time import time, sleep



#CAMBIABLE:
client = Client('<TU-API-ID>', '<TU-API-SECRET>')
tiempoActualizacion = 5

#PREDEFINIDOS:
vecesQueCambia = 0
valorMoneda = "EUR: 69"
tiempoSecs = vecesQueCambia*tiempoActualizacion-tiempoActualizacion
tiempoSecss = tiempoSecs
tiempoMins = 0
valorMin = 0
valorMax= 0

#TEXTO
def PonerTexto():
    os.system("cls")                                                
    print("                                                         ")
    print(" ________           __                          __       ")
    print("/        |         /  |                        /  |      ")
    print("$$$$$$$$/______   _$$ |_    __    __   _______ $$ |   __ ")
    print("   $$ | /      \ / $$   |  /  |  /  | /       |$$ |  /  |")
    print("   $$ | $$$$$$  |$$$$$$/   $$ |  $$ |/$$$$$$$/ $$ |_/$$/ ")
    print("   $$ | /    $$ |  $$ | __ $$ |  $$ |$$ |      $$   $$<  ")
    print("   $$ |/$$$$$$$ |  $$ |/  |$$ \__$$ |$$ \_____ $$$$$$  \ ")
    print("   $$ |$$    $$ |  $$  $$/ $$    $$/ $$       |$$ | $$  |")
    print("   $$/  $$$$$$$/    $$$$/   $$$$$$/   $$$$$$$/ $$/   $$/  API by Coinbase Developers <3")
    print( )
    
#BUCLE VALOR WALLET
def realTimeEscritura(walletID):
  #LLAMADAS A VARIABLE
  global valorMoneda
  valorMoneda = client.get_account(walletID)
  #MAXIMO Y MINIMO PREDEFINIDOS
  global valorMin
  global valorMax

  valorMin = valorMoneda.native_balance.amount
  valorMax = valorMoneda.native_balance.amount

  while True:
    sleep(tiempoActualizacion - time() % tiempoActualizacion)
    global vecesQueCambia
    vecesQueCambia = vecesQueCambia + 1
    global tiempoSecss
    global tiempoMins
    global tiempoSecs
    tiempoSecs = vecesQueCambia*tiempoActualizacion-tiempoActualizacion
    valorMoneda = client.get_account(walletID)
    #TIEMPO
    
    #MINUTOS  
    if tiempoSecs >= 3600:
        
        tiempoMins = tiempoSecs//60 - tiempoSecs//3600*60
    else:
      tiempoMins = tiempoSecs//60

    #SEGUNDOS
    if tiempoSecs >= 60:
        
        tiempoSecss = tiempoSecs - (tiempoSecs//60*60)
    else:
      tiempoSecss = tiempoSecs
    
    

    #MAXIMO Y MINIMO
    
    if float(valorMoneda.native_balance.amount)>float(valorMax):
        
        valorMax = float(valorMoneda.native_balance.amount)
    if float(valorMoneda.native_balance.amount)<float(valorMin):
        
        valorMin = float(valorMoneda.native_balance.amount)

    #ESCRITURA
    PonerTexto()
    
    print( )
    print("__________________________________________________________________________")
    print("| Valor a tiempo medianamente real de " + valorMoneda.balance.currency +" en " + valorMoneda.native_balance.currency + ":")
    print("| " + valorMoneda.native_balance.amount + " : " +valorMoneda.native_balance.currency)
    print("| MAX: "+str(valorMax)+ " : " +valorMoneda.native_balance.currency+" | MIN: "+ str(valorMin)+ " : " +valorMoneda.native_balance.currency)
    print("|_________________________________________________________________________")
    print( )
    print("__________________________________________________________________________")
    print("| Veces que se ha actualizado: "+str(vecesQueCambia))
    print("| Tiempo funcionando: " + str(tiempoSecs//3600)+ "h, " + str(tiempoMins) + "min, " + str(tiempoSecss) + "sec")
    print("| Nombre de la wallet: "+ valorMoneda.name)
    print("|_________________________________________________________________________")
  
#CREAR WALLET
def CrearWallet():
    PonerTexto()
    walletIDElegido = input("Cual es el ID de tu wallet: ")
    try:
        walletID = walletIDElegido
        global valorMoneda
        valorMoneda = client.get_account(walletID)
        try:
            os.mkdir("wallets")
        except:
            pass
        wallet = open("wallets/"+valorMoneda.name+".wallet","w") 
        wallet.write(walletIDElegido)
        wallet.close()
        print("Creada con el nombre: "+ valorMoneda.name+ "!! :D")
        print()
    except(KeyboardInterrupt):
        pass
    except:
        print("HUBO UN ERROR!!! PODRIA SER QUE NO EXISTE ESE ID DE TU WALLET, O TIENES MAL PUESTO TU CLIENT-ID o CLIENT-SECRET")
    print("Quieres seguir con el programa?")
    print("[0] Si :D")
    print("[1] Obtener IDs")
    print("[2] No, salir")
    eleccion = input("Que eliges? ")
    if eleccion == "0":
        ElegirWallet()
    elif eleccion == "1":
        ObtenerID()
    else:
        exit

#ELIMINAR WALLET
def EliminarWallet():
    PonerTexto()
    print("Cual Wallet quieres eliminar?")
    walletsLista = os.listdir("wallets")
    walletsListaCantidad = 0
    for x in walletsLista:
        print("["+str(walletsListaCantidad)+"]ELIMINAR: "+walletsLista[walletsListaCantidad].replace(".wallet", ""))
        walletsListaCantidad = walletsListaCantidad + 1
    print("["+str(walletsListaCantidad)+"]"+"Salir :D")
    walletElegidaNumero = input("Elija una wallet: ")
    walletElegidaNumero = int(walletElegidaNumero)
    if walletElegidaNumero == walletsListaCantidad:
        ElegirWallet()
    else:
        PonerTexto()
        os.remove("wallets/"+walletsLista[walletElegidaNumero])
        print("Wallet: " + walletsLista[walletElegidaNumero]+" ELIMINADA!!!! :D")
        print("Quieres seguir con el programa?")
        print("[0] Si :D")
        print("[1] No, salir")
        eleccion = input("Que eliges? ")
        if eleccion == "0":
            ElegirWallet()
        else:
            exit

#OBTENER IDs
def ObtenerID():
    PonerTexto()
    
    listaIDs = client.get_accounts()
    cantidadIDs = len(listaIDs.data)
    print(cantidadIDs)
    try:
        print("  ______________________________________________________________________________")
        print(" /_____________________________________________________________________________/")
        print("/_____________________________________________________________________________/")
        while cantidadIDs >= 0:
            
            walletIDs = listaIDs[cantidadIDs-1]
            print("|| #"+str(cantidadIDs))
            print("|| Nombre Wallet: "+walletIDs.name)
            print("|| Moneda de la Wallet: "+ walletIDs.balance.currency)
            print("|| ID Wallet: "+ walletIDs.id)
            print("|| Balance Wallet: "+walletIDs.balance.amount)
            print("|| Balance Wallet a "+ walletIDs.native_balance.currency + ":"+ walletIDs.native_balance.amount)
            print("|| Creada en: "+ walletIDs.created_at)
            print("|| Ultima vez actualizada: "+walletIDs.updated_at)
            if cantidadIDs == 0:
                print("||_____________________________________________________________________________")
                print("| SI NO VES LA WALLET QUE BUSCABAS ASEGURATE DE QUE LA API TENGA ACCESO A ELLA!")
                print("\______________________________________________________________________________")
            else:
                print("||-----------------------------------------------------------------------------")
            cantidadIDs = cantidadIDs - 1
    except:
        pass
        
#VER VALOR CRIPTOMONEDAS
def VerValorCriptomonedas():
   PonerTexto()
    
   listaIDs = client.get_accounts()
   cantidadIDs = len(listaIDs.data)
   
   try:
       print("   ___ __  ___ __ ___ ___  __  __  ___          ___  _    ___  ___")
       print("  /   /_/  /  /_/ /  /  / / /_/ / /  /  /\  /  /__  / \  /__/ /__")
       print(" /__ / / _/_ /   /  /__/ /     / /__/  /  \/  /___ /__/ /  / ___/ ")
       print()
       print(" _____________________________________________________________________________")
       print("/ ____________________________________________________________________________\ ")
       while cantidadIDs > 0:
           
           walletIDs = listaIDs[cantidadIDs-1]
           print("|| ["+str(cantidadIDs)+"]Moneda: "+ walletIDs.balance.currency)
           
           
           if cantidadIDs >= 0:
               cantidadIDs = cantidadIDs - 1
               
       print("||_____________________________________________________________________________")
       print("\_____________________________________________________________________________/")
   except:
        print("HUBO UN ERROR OBTENIENDO TUS CRIPTOMONEDAS! ASEGURATE DE QUE LA CLIENT-ID/SECRET ESTEN BIEN PUESTOS O QUE EN LA CONFIGURACION DE LA API HAY ACCESO A LAS WALLETS! -> https://www.coinbase.com/settings/api")
   print()
   print("Seleciona la moneda que quieres ver! :D")
   print("Si no ves alguna moneda asegurate que en la configuracion de la API hay acceso a las wallets -> https://www.coinbase.com/settings/api")
   monedaSeleccionadaNum= input("Numero de la moneda: ")
   monedaSeleccionada = listaIDs[int(monedaSeleccionadaNum)-1].balance.currency
   monedaRegional = listaIDs[0].native_balance.currency

   #print(client.get_buy_price(currency_pair = monedaSeleccionada+"-"+monedaRegional))
   #LLAMADAS A VARIABLE
   global valorMoneda
   valorMoneda = client.get_buy_price(currency_pair = monedaSeleccionada+"-"+monedaRegional)
   #MAXIMO Y MINIMO PREDEFINIDOS
   global valorMin
   global valorMax
              
   valorMin = valorMoneda.amount
   valorMax = valorMoneda.amount
   
   while True:
     sleep(5 - time() % 5)
     global vecesQueCambia
     vecesQueCambia = vecesQueCambia + 1
     global tiempoSecss
     global tiempoMins
     global tiempoSecs
     tiempoSecs = vecesQueCambia*tiempoActualizacion-tiempoActualizacion
     valorMoneda = client.get_buy_price(currency_pair = monedaSeleccionada+"-"+monedaRegional)
   
     #TIEMPO
     
     #MINUTOS  
     if tiempoSecs >= 3600:
         
         tiempoMins = tiempoSecs//60 - tiempoSecs//3600*60
     else:
       tiempoMins = tiempoSecs//60
   
     #SEGUNDOS
     if tiempoSecs >= 60:
         
         tiempoSecss = tiempoSecs - (tiempoSecs//60*60)
     else:
       tiempoSecss = tiempoSecs
     
     
   
     #MAXIMO Y MINIMO
     
     if float(valorMoneda.amount)>float(valorMax):
         
         valorMax = float(valorMoneda.amount)
     if float(valorMoneda.amount)<float(valorMin):
         
         valorMin = float(valorMoneda.amount)
   
     #ESCRITURA
     PonerTexto()
     
     print( )
     print("__________________________________________________________________________")
     print("| Valor a tiempo medianamente real de " + valorMoneda.base +" en " + valorMoneda.currency + ":")
     print("| " + valorMoneda.amount + " : "+ valorMoneda.currency)
     print("| MAX: "+str(valorMax)+ " : " +valorMoneda.currency+" | MIN: "+ str(valorMin)+ " : " +valorMoneda.currency)
     print("|_________________________________________________________________________")
     print( )
     print("__________________________________________________________________________")
     print("| Veces que se ha actualizado: "+str(vecesQueCambia))
     print("| Tiempo funcionando: " + str(tiempoSecs//3600)+ "h, " + str(tiempoMins) + "min, " + str(tiempoSecss) + "sec")
     print("|_________________________________________________________________________")
     

#ELEGIR WALLET
def ElegirWallet():
    PonerTexto()
    try:
        print("Que Wallet quieres usar?")
        walletsLista = os.listdir("wallets")
        walletsListaCantidad = 0
        for x in walletsLista:
            
            print("["+str(walletsListaCantidad)+"]"+walletsLista[walletsListaCantidad].replace(".wallet", ""))
            walletsListaCantidad = walletsListaCantidad + 1
        print("["+str(walletsListaCantidad)+"]"+"Crear una nueva :D")
        print("["+str(walletsListaCantidad+1)+"]"+"Obtener IDs Wallets")
        print("["+str(walletsListaCantidad+2)+"]"+"Ver valor criptomonedas")
        print("["+str(walletsListaCantidad+3)+"]"+"Eliminar una Wallet guardada")
        walletElegidaNumero = input("Elija una wallet: ")
        walletElegidaNumero = int(walletElegidaNumero)
        if walletElegidaNumero == walletsListaCantidad:
            CrearWallet()
        
        elif walletElegidaNumero == walletsListaCantidad+1:
            ObtenerID()

        elif walletElegidaNumero == walletsListaCantidad+2:
            VerValorCriptomonedas()
        elif walletElegidaNumero == walletsListaCantidad + 3:
            
            EliminarWallet()
        else:

            walletElegidaArchivo = open("wallets/"+walletsLista[walletElegidaNumero],"r")
            walletIDElegido=walletElegidaArchivo.read()
            
            
            
            realTimeEscritura(walletIDElegido)
    except(FileNotFoundError):
        print("HUBO UN ERROR!!! NO HAY WALLETS PUESTAS!! INTENTA REINICIAR EL PROGRAMA!")
        pass

#VER SI HAY WALLETS
try:
    walletsLista = os.listdir("wallets")
    if walletsLista[0] == walletsLista[0]:
        ElegirWallet()
        
        #print("TRY-1")
        
    else:
        CrearWallet()
        #print("TRY-0")


except(KeyboardInterrupt):
    pass
except(IndexError):
    CrearWallet()
except:
    CrearWallet()





    


