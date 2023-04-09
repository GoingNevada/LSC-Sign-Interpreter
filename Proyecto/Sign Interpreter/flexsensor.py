#-----------LIBRERIAS---------------
import serial # Libreria para la obtencion de datos por medio de comunicacion bluetooth

#-------VARIABLES GLOBALES----------
ser = None


#-----CONFIGURACION COMUNICACION BLUETOOTH----

def bluetooth():
    try:
        global ser
        ser = serial.Serial('COM4',115200)
        ser.write('1'.encode('utf-8'))
        return True
    except:
        return False

#--------INICIALIZACION DE CAMARA----------

def adc():
    global ser

    hand_data = [0,0,0,0,0]
    lecturas = []
    sign = "_"
    # RECEPCION DE DATOS POR BLUETOOTH
    if ser.readable():
        cadena = ser.readline().decode().strip()
        sensores = cadena.split(",")
        lecturas = list(map(int,sensores))

    hand_data[0] = lecturas[0] # PULGAR
    hand_data[1] = lecturas[1] # INDICE
    hand_data[2] = lecturas[2] # CORAZON
    hand_data[3] = lecturas[3] # ANULAR
    hand_data[4] = lecturas[4] # MEÑIQUE

    # PARAMETROS PARA EL RECONOCIMIENTO DE NUMERO DEL 1-5
    if 500<hand_data[0]<700 and 700<hand_data[1]<900 and 200<hand_data[2]<400 and 200<hand_data[3]<400 and 200<hand_data[4]<400:
        sign = "1"
    elif 700<hand_data[0]<900 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 200<hand_data[3]<450 and 200<hand_data[4]<450:
        sign = "2"
    elif 600<hand_data[0]<800 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 700<hand_data[3]<950 and 200<hand_data[4]<450:
        sign = "3"
    elif 800<hand_data[0]<980 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 700<hand_data[3]<950 and 600<hand_data[4]<850:
        sign = "4"
    elif 980<hand_data[0]<1100 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 700<hand_data[3]<950 and 600<hand_data[4]<850:
        sign = "5"

    # PARAMETROS PARA EL RECONOCIMIENTO DE LAS VOCALES
    elif 900<hand_data[0]<1100 and 300<hand_data[1]<500 and 200<hand_data[2]<400 and 200<hand_data[3]<400 and 100<hand_data[4]<300:
        sign = "A"
    elif 500<hand_data[0]<700 and 200<hand_data[1]<400 and 200<hand_data[2]<400 and 200<hand_data[3]<400 and 100<hand_data[4]<300:
        sign = "E"
    elif 500<hand_data[0]<700 and 400<hand_data[1]<600 and 200<hand_data[2]<400 and 300<hand_data[3]<500 and 700<hand_data[4]<900:
        sign = "I"
    elif 600<hand_data[0]<800 and 400<hand_data[1]<600 and 200<hand_data[2]<500 and 400<hand_data[3]<600 and 300<hand_data[4]<500:
        sign = "O"
    elif 800<hand_data[0]<1100 and 700<hand_data[1]<900 and 200<hand_data[2]<400 and 300<hand_data[3]<500 and 700<hand_data[4]<900:
        sign = "U"
    
    # PARAMTROS PAR EL RECONOCIMIENTO DEL ABECEDARIO
    elif 500<hand_data[0]<700 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 700<hand_data[3]<950 and 600<hand_data[4]<850:
        sign = "B"
    elif 800<hand_data[0]<1000 and 500<hand_data[1]<700 and 300<hand_data[2]<500 and 400 <hand_data[3]<600 and 400<hand_data[4]<600:
        sign = "C"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 300<hand_data[2]<500 and 400<hand_data[3]<600 and 400<hand_data[4]<600:
        sign = "D"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 300<hand_data[2]<500 and 300<hand_data[3]<500 and 100<hand_data[4]<300:
        sign = "F"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 200<hand_data[3]<450 and 200<hand_data[4]<450:
        sign = "K" 
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 200<hand_data[2]<400 and 300<hand_data[3]<500 and 200<hand_data[4]<400:
        sign = "L"
    elif 600<hand_data[0]<800 and 600<hand_data[1]<800 and 400<hand_data[2]<600 and 500<hand_data[3]<700 and 200<hand_data[4]<400:
        sign = "M"
    elif 600<hand_data[0]<800 and 600<hand_data[1]<800 and 400<hand_data[2]<600 and 300<hand_data[3]<500 and 200<hand_data[4]<400:
        sign = "N"
    elif 900<hand_data[0]<1100 and 400<hand_data[1]<600 and 600<hand_data[2]<800 and 300<hand_data[3]<500 and 300<hand_data[4]<500:
        sign = "P"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 400<hand_data[2]<600 and 500<hand_data[3]<700 and 400<hand_data[4]<600:
        sign = "Q"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 500<hand_data[2]<700 and 300<hand_data[3]<500 and 200<hand_data[4]<400:
        sign = "R"
    elif 900<hand_data[0]<1100 and 500<hand_data[1]<700 and 800<hand_data[2]<1000 and 800<hand_data[3]<1000 and 700<hand_data[4]<900:
        sign = "T"
    elif 500<hand_data[0]<700 and 700<hand_data[1]<950 and 700<hand_data[2]<950 and 200<hand_data[3]<450 and 200<hand_data[4]<450:
        sign = "V"
    elif 900<hand_data[0]<1100 and 700<hand_data[1]<900 and 700<hand_data[2]<900 and 700<hand_data[3]<900 and 300<hand_data[4]<500:
        sign = "W"
    elif 600<hand_data[0]<800 and 400<hand_data[1]<600 and 200<hand_data[2]<400 and 200<hand_data[3]<400 and 200<hand_data[4]<400:
        sign = "X"
    elif 900<hand_data[0]<1100 and 400<hand_data[1]<600 and 300<hand_data[2]<500 and 300<hand_data[3]<500 and 700<hand_data[4]<900:
        sign = "Y"
    
    return sign

def endbluetooth():
    global ser
    if ser is not None:
        ser.write('0'.encode('utf-8'))
        ser.close()