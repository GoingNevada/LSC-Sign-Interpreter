"""
Con el codigo escrito en este .py, crearemos la base de datos 
necesaria para generar datos de entrada, que funcionaran para 
el posterior aprendizaje del modelo de entranmiento del clasificador 
que se utilizara para diferenciar las señas estaticas que se 
realizan en tiempo real
"""

#-----------LIBRERIAS---------------
import cv2 # Open CV para utilizacion y manejo de imagenes y vision artificial 
import numpy as np # Libreria de calculo y manejo de datos de tipo vector y matrices
import serial # Libreria para la obtencion de datos por medio de protocolo RS232
import pandas as pd # Libreria especializada en la creacion y manejo de datos en diferentes formatos
import os # Libreria de conexion al os para creacion y manejor de archivos

wrd = ""
flag = 0

def letter(sign):
    global wrd, flag
    if sign==wrd:
        flag = flag + 1
        if flag>40:
            print(sign)
            flag = 0
    else:
        wrd=sign
        flag = 0

#-----CONFIGURACION COMUNICACION BLUETOOTH----

try:
    ser = serial.Serial('COM4',115200)
    print('Conexion exitosa')
    ser.write('1'.encode('utf-8'))
except:
    print('Error de conexion')

#--------INICIALIZACION DE CAMARA----------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == False: break
    height, width, _ = frame.shape  # x=640 y=480
    frame = cv2.flip(frame, 1)
    hand_data = [0, # 0 angle1
                 0, # 1 angle2
                 0, # 2 angle3
                 0, # 3 angle4
                 0] # 4 angle5
        
    lecturas = []
    sign = "_"

    # RECEPCION DE DATOS POR RS232
    if ser.readable():
        cadena = ser.readline().decode().strip()
        sensores = cadena.split(",")
        lecturas = list(map(int,sensores))

    # ASIGNACION DE ANGULOS INTERNOS DE CADA DEDO
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
    
    letter(sign)

    # VISUALIZACION
    cv2.rectangle(frame, (0, 0), (640, 60), (223, 134, 21), -1)
    cv2.rectangle(frame, (540, 0), (640, 60), (125, 220, 0), -1)
    cv2.putText(frame, sign, (570, 55), 1, 5, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(frame, 'Ap:', (20, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, str(hand_data[0]), (60, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, 'Ai:', (120, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, str(hand_data[1]), (160, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, 'Ac:', (220, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, str(hand_data[2]), (260, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, 'Aa:', (320, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, str(hand_data[3]), (360, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, 'Am:', (420, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, str(hand_data[4]), (460, 35), 1, 1, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1)==27: break

cap.release()
ser.write('0'.encode('utf-8'))
ser.close()
cv2.destroyAllWindows()

