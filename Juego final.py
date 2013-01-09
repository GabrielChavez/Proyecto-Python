#!\C:\Python27

import pygame, pygame.mixer, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init

screen = pygame.display.set_mode((300, 300))

pygame.mixer.music.load("C:/Users/pc/Desktop/Cuento/Danubio azul.wav")
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play(-1, 0.0)

inicio = pygame.mixer.Sound("1_Inicio.wav")
inicio.play()
pygame.time.wait(24000)

#Seleccionas una opcion
while True:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_a:
            derecha = pygame.mixer.Sound("2_derecha.wav")
            derecha.play()
            pygame.time.wait(35000)
        
            #Seleccionas una opcion
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN and event.key == K_a:
                        a = pygame.mixer.Sound("3_analizas la cueva.wav")
                        a.play()
                        pygame.time.wait(26000)
                    
                        #Seleccionas una opcion
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                elif event.type == KEYDOWN and event.key == K_a:
                                    a = pygame.mixer.Sound("5_vas hacia el agua.wav")
                                    a.play()
                                    pygame.time.wait(49000)

                                    #Seleccionas una opcion
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_a:
                                                a = pygame.mixer.Sound("6_nadas contracorriente_fin.wav")
                                                a.play()
                                                pygame.time.wait(28000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_b:
                                                b = pygame.mixer.Sound("7_te dejas llevar.wav")
                                                b.play()
                                                pygame.time.wait(31000)
                
                                                #Seleccionas una opcion
                                                while True:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            sys.exit()
                                                        elif event.type == KEYDOWN and event.key == K_a:
                                                            a = pygame.mixer.Sound("9_vas a la casa_fin.wav")
                                                            a.play()
                                                            pygame.time.wait(34000)
                                                            #Para salir definitivamente del juego apenas termine el audio.
                                                            sys.exit()
                                                        elif event.type == KEYDOWN and event.key == K_b:
                                                            b = pygame.mixer.Sound("8_te acuestas y esperas_fin.wav")
                                                            b.play()
                                                            pygame.time.wait(20000)
                                                            #Para salir definitivamente del juego apenas termine el audio.
                                                            sys.exit()
                                    
                                elif event.type == KEYDOWN and event.key == K_b:
                                    b = pygame.mixer.Sound("10_vas a la luz.wav")
                                    b.play()
                                    pygame.time.wait(32000)

                                    #Seleccionas una opcion
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_a:
                                                a = pygame.mixer.Sound("11_continuas hacia la luz_fin.wav")
                                                a.play()
                                                pygame.time.wait(37000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_b:
                                                b = pygame.mixer.Sound("12_regresas hacia la cueva_fin.wav")
                                                b.play()
                                                pygame.time.wait(46000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                
                    elif event.type == KEYDOWN and event.key == K_b:
                        b = pygame.mixer.Sound("4_regresas por el tunel_fin.wav")
                        b.play()
                        pygame.time.wait(23000)
                        #Para salir definitivamente del juego apenas termine el audio.
                        sys.exit()
                    
        elif event.type == KEYDOWN and event.key == K_b:
            izq = pygame.mixer.Sound("13_izquierda.wav")
            izq.play()
            pygame.time.wait(37000)
    
            #Seleccionas una opcion
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN and event.key == K_a:
                        a = pygame.mixer.Sound("25_entras en la selva.wav")
                        a.play()
                        pygame.time.wait(30000)
        
                        #Seleccionas una opcion
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                elif event.type == KEYDOWN and event.key == K_a:
                                    a = pygame.mixer.Sound("26_sigues avanzando_fin.wav")
                                    a.play()
                                    pygame.time.wait(59000)
                                    #Para salir definitivamente del juego apenas termine el audio.
                                    sys.exit()
                                elif event.type == KEYDOWN and event.key == K_b:
                                    b = pygame.mixer.Sound("27_te quedas.wav")
                                    b.play()
                                    pygame.time.wait(69000)

                                    #Seleccionas una opcion
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_a:
                                                a = pygame.mixer.Sound("11_continuas hacia la luz_fin.wav")
                                                a.play()
                                                pygame.time.wait(37000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_b:
                                                b = pygame.mixer.Sound("28_regresas a la cueva_fin.wav")
                                                b.play()
                                                pygame.time.wait(46000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                     
                    elif event.type == KEYDOWN and event.key == K_b:
                        b = pygame.mixer.Sound("14_entras al edificio.wav")
                        b.play()
                        pygame.time.wait(30000)

                        #Seleccionas una opcion
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                elif event.type == KEYDOWN and event.key == K_a:
                                    a = pygame.mixer.Sound("22_subes por el ascensor.wav")
                                    a.play()
                                    pygame.time.wait(39000)

                                    #Seleccionas una opcion
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_a:
                                                a = pygame.mixer.Sound("23_tomas la roja_fin.wav")
                                                a.play()
                                                pygame.time.wait(31000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_b:
                                                b = pygame.mixer.Sound("24_tomas la azul_fin.wav")
                                                b.play()
                                                pygame.time.wait(21000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()
                                     
                                elif event.type == KEYDOWN and event.key == K_b:
                                    b = pygame.mixer.Sound("15_vas hacia el bar.wav")
                                    b.play()
                                    pygame.time.wait(41000)
            
                                    #Seleccionas una opcion
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                sys.exit()
                                            elif event.type == KEYDOWN and event.key == K_a:
                                                a = pygame.mixer.Sound("16_sigues escuchando.wav")
                                                a.play()
                                                pygame.time.wait(42000)
                
                                                #Seleccionas una opcion
                                                while True:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            sys.exit()
                                                        elif event.type == KEYDOWN and event.key == K_a:
                                                            a = pygame.mixer.Sound("18_le dices la clave_fin.wav")
                                                            a.play()
                                                            pygame.time.wait(25000)
                                                            #Para salir definitivamente del juego apenas termine el audio.
                                                            sys.exit()
                                                        elif event.type == KEYDOWN and event.key == K_b:
                                                            b = pygame.mixer.Sound("19_no le dices la clave.wav")
                                                            b.play()
                                                            pygame.time.wait(50000)
                    
                                                            #Seleccionas una opcion
                                                            while True:
                                                                for event in pygame.event.get():
                                                                    if event.type == pygame.QUIT:
                                                                        sys.exit()
                                                                    elif event.type == KEYDOWN and event.key == K_a:
                                                                        a = pygame.mixer.Sound("20_corres al ascensor_fin.wav")
                                                                        a.play()
                                                                        pygame.time.wait(41000)
                                                                        #Para salir definitivamente del juego apenas termine el audio.
                                                                        sys.exit()
                                                                    elif event.type == KEYDOWN and event.key == K_b:
                                                                        b = pygame.mixer.Sound("21_corres a la entrada_fin.wav")
                                                                        b.play()
                                                                        pygame.time.wait(39000)
                                                                        #Para salir definitivamente del juego apenas termine el audio.
                                                                        sys.exit()
                                                
                                            elif event.type == KEYDOWN and event.key == K_b:
                                                b = pygame.mixer.Sound("17_te alejas de Charles_fin.wav")
                                                b.play()
                                                pygame.time.wait(30000)
                                                #Para salir definitivamente del juego apenas termine el audio.
                                                sys.exit()

