import pygame

from core.level import World
from entities.player import Player
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Plataforma")

    def run(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        tiempo_animacion = 0

        mundo = World()

        player = Player()

        character_state = CHARACTER_STATE_IDLE
        character_oriantation = ORIANTATION_RIGHT

        running = True
        while running:

            #devuelve el numero de SEGUNDOS( /1000) transcurridos desde el ultimo tick hasta este(.016 s)
            dt = clock.tick(FPS)/1000
            tiempo_animacion += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #Evaluo si me estoy moviendo a la izquierda o derecha
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-(300*dt),0,screen)
                character_state = CHARACTER_STATE_RUN
                character_oriantation = ORIANTATION_LEFT

            if keys[pygame.K_RIGHT]:
                player.move(300*dt,0,screen)
                character_state = CHARACTER_STATE_RUN
                character_oriantation = ORIANTATION_RIGHT

            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] or not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                character_state = CHARACTER_STATE_IDLE

            if keys[pygame.K_UP]:
                player.jump()

            #Evaluo si esta cayendo o no
            if player.Vy < 0:
                character_state = CHARACTER_STATE_JUMP
            if player.Vy > 0:
                character_state = CHARACTER_STATE_FALL

            mundo.draw(screen)
            player.draw(screen)

            player.aplicar_gravedad(dt)

            while tiempo_animacion >= TIEMPO_POR_FRAME:
                player.actualizar_fotograma(character_state,character_oriantation)
                #recuperamos sin reiniciar el contador, para que se sincronize
                tiempo_animacion -= TIEMPO_POR_FRAME
            pygame.display.flip()