
#Con este codigo se puede descargar el osm de el seibo desde openstreetmap
"""
import requests

# URL de la región deseada y parámetros de descarga
url = 'https://api.openstreetmap.org/api/0.6/map?bbox=-69.2161,18.7596,-68.9113,19.0193'
headers = {'User-Agent': 'Mozilla/5.0'}

# Hacer solicitud GET y guardar datos en archivo
response = requests.get(url, headers=headers)
with open('seibo.osm', 'wb') as f:
    f.write(response.content)
    """
# Linea para importar librerias como que se utilizaran (Tkinter esto para crear la GUI), (OpenStreetMap realiza la busqueda de la ruta) 
# Tambien se importan varias librerias de TK y de otras librerias para ser usada en el GUI

from cgitb import text
from ctypes.wintypes import SIZE
from pickle import READONLY_BUFFER
from re import T, X
from tkinter import Tk, Label, Button, Entry
from tkinter import font
from tkinter.font import Font
from turtle import bgcolor, color, width
from typing import Text
import tkinter.font as tkFont
from colorama import Style
from pyparsing import col
import openstreetmap
from tkhtmlview import *
from openstreetmap import labuscanodos3000

import osmnx as ox

# def suma():
#     n1=txt.get()
#     n2=txt.get()

#     r=float(n1) + float(n2)
#     txt3.insert(0,r)

coordenada1 =  None
coordenada2 = None

#Se crea la ventana de con el titulo de MAPROUTING
Ventana = Tk()
Ventana.title("MapRouting")
Ventana.geometry("800x600")
Ventana.config(bg="#1e1e1e")

# Se define la fuente para el título
titulo_font = Font(family="Arial", size=36, weight="bold")

# Se agrega un título a la ventana
titulo = Label(Ventana, text="Map Routing", font=titulo_font, bg="#1e1e1e", fg="white")
titulo.pack(pady=50)

# Se crean dos campos para que el usuario pueda entrar las coordenadas que desea consultar
coordenadas_font = Font(family="Arial", size=18)

coordenadas_texto = Label(Ventana, text="Ingresa las coordenadas:", font=coordenadas_font, bg="#1e1e1e", fg="white")
coordenadas_texto.pack()

txt1 = Entry(Ventana, font=coordenadas_font)
txt1.pack(pady=10)

txt2 = Entry(Ventana, font=coordenadas_font)
txt2.pack(pady=10)

# Aqui se define la funcion ejecutar, la cual funcionara con un boton
# Los valores pasan a la funcion OpenStreetMap.main para buscar la ruta mas cercan.
# Si encuentra la ruta mas cercana sera enviado a un enlace con la ruta en un mapa en linea y si hay un error presentara un mensaje




def ejecutar():
    
        coordenada1 = txt1.get()
        coordenada2 = txt2.get()


        resultado = labuscanodos3000(coordenada1, coordenada2)

        #link = HTMLLabel(Ventana, html=f'<div style="text-align: center;"><a href="{resultado}" style="color: dodgerblue; text-align: left; width: 50px; height: 20px;">Abrir en el mapa</a></div>')
        #link.config(width="20", height="2", background="#1e1e1e", foreground="white")
        #link.pack(pady=50)

    

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# Se crea el botón de ejecutar con un estilo personalizado
btn_font = Font(family="Arial", size=18, weight="bold")
btn = Button(text="Ejecutar", command=ejecutar, font=btn_font, width=20, height=2, bg="dodgerblue", fg="white", activebackground="deepskyblue")
btn.pack(pady=50)


Ventana.mainloop()