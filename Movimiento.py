# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 300,500            # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño) # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Gravedad")      # Se le pone un nombre al borde de la pantalla

# -DATOS DE LA PELOTA 
class Pelota:

    def __init__(self, x , y , radio , color):
        self.x      = x
        self.y      = y
        self.radio  = radio
        self.color  = color
        self.grosor = 0 

    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

# -DATOS
velocidad = 0
altura    = 150 
toco_piso = False

balon = Pelota ( 150 , 20 , 20 , rojo)
# -BUCLÉ 
while True:
    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()
        if accion.type    == pygame.KEYDOWN:
            # Si presionamos la tecla 'c'
            if accion.key == pygame.K_c:
               velocidad = 20 

    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)

    # Movimiento en el eje Y
    balon.y += velocidad 

    # Muestra la pelota
    balon.mostrar()
    # Lineas de medición BORRAR DESPUÉS XXXXXXXXXXXXXXXXXXX
    #L1 = pygame.draw.line(pantalla, negro, (0,150), (300,150))
    #L2 = pygame.draw.line(pantalla, negro, (0,225), (300,225))

    # Condición para no rebasar el suelo
    if balon.y >= alto:
        velocidad *= -1
        toco_piso = True

    # Si la pelota llego al piso rebotara y cada vez perdera altura hasta quedar quieta
    elif toco_piso == True and balon.y <= altura:
        velocidad *= -1
        toco_piso = False
       
       # Cada vez que rebota pierde altura
        if altura <= alto:
            altura += 20 

        # Si la pelota esta en el piso sin velocidad se queda quieta
        elif altura >= alto:
            velocidad = 0



    # Manejo de la pantalla
    pygame.display.update()

    # Actualización de la pantalla
    pygame.time.delay(30)
