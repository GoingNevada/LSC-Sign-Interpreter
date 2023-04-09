# LIBRERIAS
from tkinter import *
from tkinter.messagebox import *
import cv2
import matplotlib as mplt
import numpy as np
import imutils
from PIL import Image, ImageTk
import serial
from flexsensor import *

# FUNCIONES
def visualizar():
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            # x=640 y=480
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)
            frame = imutils.resize(frame, width=640)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblvideo.configure(image=img)
            lblvideo.image = img
            lblvideo.after(5, visualizar)
        else:
            global videobutton
            videobutton.config(bg="green", text="Activar Camara")
            img = PhotoImage(file="EntornoVirtual/foto.png")
            lblvideo.config(image=img)
            cap.release()

def video():
    global cap, videobutton, bluetbutton
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    visualizar()
    bluetbutton.config(state='normal', bg="blue")
    videobutton.config(bg="red", text="Desactivar Camara")

def comunicacion():
    global palabra
    if blue==True:
        letra = adc()
        lblLetra.configure(text=letra)
        lblLetra.after(10, comunicacion)
    else:
        endbluetooth()
        bluetbutton.config(bg="blue", text="Conectar Guante")
        

def conexion():
    global bluetbutton, blue
    blue = bluetooth()
    if blue==True:
        showinfo("Conexion Guante","Dispoitivo conectado con exito")
    else:
        showwarning("Conexion Guante","No se ha podido establecer una conexion con el dispositivo")
    comunicacion()
    bluetbutton.config(bg="red",text="Desconectar Guante")

    
    
# VARIABLES GLOBALES
palabra = ""
videobutton = None
lblvideo = None
lblLetra = None
cap = None
bluetbutton = None
blue = None
lblEscri = None

# VENTANA PRINCIPAL
Frame = Tk()
Frame.title("SIGN INTERPRETER | LENGUAJE DE SEÑAS COLOMBIANO")
Frame.geometry("948x505")
Frame.config(bg="#B6B2B2")
Frame.resizable(False,False)

# PANTALLA
tex1 = Label(Frame, text="LETRA:", bg="#B6B2B2")
tex1.place(x=785, y=20)
lblLetra = Label(Frame, text="_", bg="white", width=3, height=1, font=["Arial", 56, "bold"])
lblLetra.place(x=735, y=45)
tex2 = Label(Frame, text="Cuadro de texto", bg="#B6B2B2")
tex2.place(x=675, y=150)
lblEscri = Text(Frame, bg="white", width=31, height=10)
lblEscri.place(x=675, y=175)

# VIDEO
img = PhotoImage(file="EntornoVirtual/foto.png")
lblvideo = Label(Frame, image=img)
lblvideo.place(x=10, y=10)
videobutton = Button(Frame, text="Activar Camara", height="3", width="20", command=video, bg="green")
videobutton.place(x=725, y=350)

# BLUETOOTH
bluetbutton = Button(Frame, text="Conectar Guante", height="3", width="20", command=conexion, bg="blue")
bluetbutton.place(x=725, y=410)

Frame.mainloop()