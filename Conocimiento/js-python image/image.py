from skimage import exposure
import skimage.color as sc
import numpy as np
import cv2
import json
import sys

sys.argv[0]

cap = cv2.VideoCapture(0) #utilizamos la camara uno
ret, frame = cap.read() #guardamos el frame capturado
frame = sc.rgb2gray(frame) #convertimos a escala de grises
frame = exposure.equalize_hist(frame) #ecualizamos la imagen
image_list = frame.tolist() #convertimos el array a una lista

#creamos un diccionario, con el array y las palabras reconocidas
data = \
{
    "imagen": image_list,
    "palabra": ["hola"]
}
JSON = json.dumps(data) #convertimos el diccionario a un archivo de JSON

print(JSON)
