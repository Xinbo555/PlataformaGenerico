import os.path

from settings import *
import pygame.image


class Player:
    def __init__(self):
        #Contador para las fotogramas
        self.cont = 0

        #Posicion en el mundo
        self.x, self.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT //2

        #velocidad vertical
        self.Vy = 0

        #Importo todas las imagenes en estas listas
        self.idle_images = self.load_idle()
        self.run_images = self.load_run()
        self.jump_images = self.load_jump()
        self.fall_images = self.load_fall()

        #estado
        self.current_state = CHARACTER_STATE_IDLE

        self.image = self.idle_images[0]

    def load_idle(self):
        images = []
        for i in range(1,12):
            path = os.path.join('assets', 'images', 'character', 'idle', f'I_{i}.png')
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, CHARACTER_SIZE)
            images.append(image)
        return images

    def load_run(self):
        images = []
        for i in range(1,13):
            path = os.path.join('assets', 'images', 'character', 'run', f'R_{i}.png')
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, CHARACTER_SIZE)
            images.append(image)
        return images

    def load_jump(self):
        images = []
        path = os.path.join('assets', 'images', 'character', 'jump', 'J_1.png')
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, CHARACTER_SIZE)
        images.append(image)
        return images

    def load_fall(self):
        images = []
        path = os.path.join('assets', 'images', 'character', 'fall', 'F_1.png')
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, CHARACTER_SIZE)
        images.append(image)
        return images

    def move(self,dx, dy, screen):
        self.x = max(0, min(self.x+dx,SCREEN_WIDTH))
        self.y = max(0, min(self.y+dy,SCREEN_HEIGHT))

    def jump(self):
        if self.Vy == 0:
            self.Vy = -500

    def aplicar_gravedad(self, dt):
        gravedad = 1000
        self.Vy += gravedad*dt
        new_y = self.y
        new_y += self.Vy * dt
        new_y = min(new_y, SCREEN_HEIGHT - 64)
        if new_y == self.y:
            self.Vy = 0
        self.y = new_y

    def getVy(self):
        return self.Vy

    def actualizar_fotograma(self, state, orientation):

        if self.current_state != state:
            self.cont = -1

        self.cont +=1

        #Evaluo el estado del jugador
        if state == CHARACTER_STATE_IDLE:
            if self.cont >= 11:
                self.cont = 0
            self.image = self.idle_images[self.cont]

        if state == CHARACTER_STATE_RUN:
            if self.cont >=12:
                self.cont = 0
            self.image = self.run_images[self.cont]

        if state == CHARACTER_STATE_JUMP:
            self.cont = 0
            self.image = self.jump_images[self.cont]

        if state == CHARACTER_STATE_FALL:
            self.cont = 0
            self.image = self.fall_images[self.cont]

        #Orientacion
        #Solo oriento si mira a la izquierda, si no por defecto mira la derecha
        if orientation == ORIANTATION_LEFT:
            self.image = pygame.transform.flip(self.image,True,False)

        self.current_state = state

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
