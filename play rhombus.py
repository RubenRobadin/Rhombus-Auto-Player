from PIL import ImageGrab
import pyautogui
import keyboard

#ubicacion de donde va a aparecer el primer pixel de las flechas
left = (650,454)
right = (940,453)
up = (798,340)
down = (797,570)

while True:
    #solamente cuando apriete la letra r va a ejecutar
    if keyboard.is_pressed("r"):
        #toma todos los pixeles de la pantalla
        px = ImageGrab.grab().load()
        #color de las flechas amarrillas
        amarillo = (253,253,19)
        blanco = (253,253,253)
        jugar = amarillo

        #si una flecha viene desde arriba o una flacha azul viene desde arriba
        #compara el color de donde deberia haber una flecha con el color rgb de una flecha
        if px[up[0],up[1]] == jugar or px[up[0],up[1]] == (0,223,253):
            #apretar la flecha de arriba
            pyautogui.press('up')
            print('up')

        #si una flecha viene desde abajo o una flacha azul viene desde abajo
        if px[down[0],down[1]] == jugar or px[down[0],down[1]] == (0,223,253):
            #apretar la flecha de abajo
            pyautogui.press('down')
            print('down')

        #si una flecha viene desde la izquierda o una flacha azul viene desde la izquierda
        if px[left[0],left[1]] == jugar or px[left[0],left[1]] == (0,223,253):
            #apretar la flecha de la izquierda
            pyautogui.press('left')
            print('left')

        #si una flecha viene desde la derecha o una flacha azul viene desde la derecha
        if px[right[0],right[1]] == jugar or px[right[0],right[1]] == (0,223,253):
            #apretar la fecha de la derecha
            pyautogui.press('right')
            print('right')