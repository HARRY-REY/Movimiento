# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame,sys

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 300,500                          # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño)               # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Movimiento con flechas")      # Se le pone un nombre al borde de la pantalla

# -CLASES
class Pelota:

    def __init__(self, x , y , radio , color):
        self.x      = x
        self.y      = y
        self.radio  = radio
        self.color  = color
        self.grosor = 0 

    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

    def update(self):
        # Obtenemos la tecla presionada
        keys= pygame.key.get_pressed()

        # Manejo de teclas
        if keys[pygame.K_UP]:
            movimiento_AB = -10
            balon.y += movimiento_AB
        if keys[pygame.K_DOWN]:
            movimiento_AB = 10
            balon.y += movimiento_AB
        if keys[pygame.K_LEFT]:
            movimiento_ID = -10
            balon.x += movimiento_ID
        if keys[pygame.K_RIGHT]:
            movimiento_ID = 10
            balon.x += movimiento_ID
            
        # Condición para no rebasar el suelo
        if balon.y >= alto:
            balon.y = alto 
        # Condición para no rebasar el techo
        if balon.y <= 0:
            balon.y = 0 

        # Condición para no rebasar el lado izquierdo 
        if balon.x <= 0:
            balon.x = 0 
        # Condición para no rebasar el lado derecho 
        if balon.x >= ancho:
            balon.x = ancho 


# -DATOS
movimiento_AB = 0 # Movimiento de arriba - abajo
movimiento_ID = 0 # Movimiento de izquierda - derecha


# -OBJETOS
balon = Pelota ( 150 , 20 , 20 , rojo)

# -BUCLÉ 
while True:

    """
    El efecto se efectua simpre que se presione la tecla,
    cuando deja de ser presionada el movimiento es 0 
    """
    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()

    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)
    
    # Muestra la pelota
    balon.update()
    balon.mostrar()


    # Manejo de la pantalla
    pygame.display.update()

    # Actualización de la pantalla
    pygame.time.delay(30)
