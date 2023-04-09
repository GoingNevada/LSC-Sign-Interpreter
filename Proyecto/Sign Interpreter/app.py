# LIBRERIAS
from tkinter import Label, Checkbutton, ttk, PhotoImage, Tk
from tkinter.messagebox import showinfo, showwarning
import cv2
import imutils
from PIL import Image, ImageTk
import serial
from flexsensor import *

# FUNCIONES
def visualizar():
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Conversion de BGR a RGB
            frame = cv2.flip(frame, 1)  # Reflejamos la imagen
            frame = imutils.resize(frame, width=640)    # Conversion de imagen a x=640 y=480
            im = Image.fromarray(frame) # Convertimos la imagen tomada en un arreglo
            img = ImageTk.PhotoImage(image=im)
            lblvideo.configure(image=img)
            lblvideo.image = img
            lblvideo.after(5, visualizar)
        else:
            global videobutton
            videobutton.config(text="Activar Camara")
            img = PhotoImage(file="Fondo.png")
            lblvideo.configure(image=img)
            lblvideo.image = img
            cap.release()

def video():
    global cap, videobutton
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    visualizar()
    videobutton.config(text="Desactivar Camara")

def comunicacion():
    global palabra
    if blue==True:
        letra = adc()
        lblLetra.configure(text=letra)
        letter(letra)
        lblEscri.configure(text=palabra)
        lblLetra.after(15, comunicacion)
    else:
        endbluetooth()
        bluetbutton.config(text="Conectar Guante")
        

def conexion():
    global bluetbutton, blue
    blue = bluetooth()
    if blue==True:
        showinfo("Conexion Guante","Dispoitivo conectado con exito")
        bluetbutton.config(text="Desconectar Guante")
    else:
        showwarning("Conexion Guante","El dispositivo no está conectado")
    comunicacion()

def letter(sign):
    global wrd, flag, palabra
    if sign==wrd and sign != "_":
        flag = flag + 1
        if flag>25:
            palabra = palabra + sign
            flag = 0
    else:
        wrd=sign
        flag = 0

# VARIABLES GLOBALES
wrd = ""
palabra = ""
flag = 0
videobutton = None
lblvideo = None
lblLetra = None
cap = None
bluetbutton = None
blue = None
lblEscri = None

# VENTANA PRINCIPAL

root = Tk()
root.title("LSC INTERPRETER | INTERPRETE DE LENGUAJE DE SEÑAS COLOMBIANO")
root.geometry("948x510")
root.config(bg="#E9E8CF")
icon = PhotoImage(file="icono-32.png")
root.iconphoto(True, icon)
root.resizable(False,False)

# ORGANIZACION DE VENTANA PRINCIPAL           
root.columnconfigure(index=0, weight=1)        
root.columnconfigure(index=1, weight=1)        
root.rowconfigure(index=0, weight=1)               

# ESTILO DE VENTANA
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")

# FRAME DE VIDEO
video_frame = ttk.LabelFrame(root, text="Video", padding=(5, 5))
video_frame.pack(side="left", padx=10, pady=(5,10))
img = PhotoImage(file="Fondo.png")
lblvideo = Label(video_frame, image=img)
lblvideo.pack(fill="both")

# FRAME DE OPCIONES
widgets_frame = ttk.Frame(root)
widgets_frame.pack(side="right", ipadx=15, ipady=5)

#----LETRA Y CUADRO DE TEXTO----
letra_frame = ttk.LabelFrame(widgets_frame, text="Letra")
letra_frame.grid(row=0, column=0, pady=10)
lblLetra = Label(letra_frame, text="_", bg="white", width=3, height=1, font=["Arial", 56, "bold"])
lblLetra.pack(fill="both")

text_frame = ttk.LabelFrame(widgets_frame, text="Cuadro de texto")
text_frame.grid(row=1, column=0, pady=10)
lblEscri = Label(text_frame, bg="white", width=31, height=10)
lblEscri.pack(fill="both")

#----BOTON DE VIDEO----
videobutton = ttk.Checkbutton(widgets_frame, text="Activar Camara", style="ToggleButton", command=video)
videobutton.grid(row=2, column=0, pady=10)

#----BOTON DE BLUETOOTH----
bluetbutton = ttk.Checkbutton(widgets_frame, text="Conectar Guante", style="ToggleButton", command=conexion)
bluetbutton.grid(row=3, column=0, pady=10)

root.mainloop()
