import pygame
import random
import time
import sys
import os
import math
import pygame.mixer
from pygame.locals import *


# Inicialição

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Tamanho da tela

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("1 vs 100")

# Variáveis

clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial", 30)
bullets = []

# Cores

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dificuldade = 0
velocidade = 1
tempo = 0

# Imagens

## Por enquanto não tem

# Sons

## Por enquanto não tem

# Classes

def menu():
    run = True
    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, red, (300, 300, 200, 50))
        text = font.render("Sair", True, black)
        screen.blit(text, (370, 305))

        pygame.draw.rect(screen, green, (300, 230, 200, 50))
        text = font.render("Continuar", True, black)
        screen.blit(text, (335, 235))

        pygame.draw.rect(screen, blue, (300, 530, 200, 50))
        text = font.render("Velocidade", True, black)
        screen.blit(text, (327, 540))

        pygame.draw.rect(screen, blue, (30, 530, 200, 50))
        text = font.render("Dificuldade", True, black)
        screen.blit(text, (55, 540))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 <= event.pos[0] <= 500 and 230 <= event.pos[1] <= 280:
                        print("Play")
                        run = False
                    if 300 <= event.pos[0] <= 500 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        sys.exit()
                    if 30 <= event.pos[0] <= 230 and 530 <= event.pos[1] <= 580:
                        global dificuldade
                        dificuldade += 1
                    if 300 <= event.pos[0] <= 500 and 530 <= event.pos[1] <= 580:
                        global velocidade
                        velocidade += 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if velocidade == 1:
            if keys["right"]:
                self.rect.x += 1
            if keys["left"]:
                self.rect.x -= 1
            if keys["up"]:
                self.rect.y -= 1
            if keys["down"]:
                self.rect.y += 1
        if velocidade == 2:
            if keys["right"]:
                self.rect.x += 2
            if keys["left"]:
                self.rect.x -= 2
            if keys["up"]:
                self.rect.y -= 2
            if keys["down"]:
                self.rect.y += 2
        

        # verifica se o jogador passou do limite da tela esquerda
        if self.rect.x < 0 - self.rect.width:
            self.rect.x = 800
        # verifica se o jogador passou do limite da tela direita
        if self.rect.x > 800 + self.rect.width:
            self.rect.x = 0

        # o player nao pode passar pelo limite superior da tela nem pelo inferior
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 600 - self.rect.height:
            self.rect.y = 600 - self.rect.height

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 0
        self.speedy = 0

    def Enemy_move(self, player_rect):
        angle = math.atan2(player_rect.y - self.rect.y, player_rect.x - self.rect.x)
        self.rect.x += math.cos(angle) * 1.5
        self.rect.y += math.sin(angle) * 1.5

        # verifica se o objeto esta dentro dos limites da tela
        if self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 600 - self.rect.height:
            self.rect.y = 600 - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0



def death():
    run = True
    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, red, (300, 300, 200, 50))
        text = font.render("Sair", True, black)
        screen.blit(text, (370, 305))

        pygame.draw.rect(screen, green, (300, 230, 200, 50))
        text = font.render("Restart", True, black)
        screen.blit(text, (335, 235))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 <= event.pos[0] <= 500 and 230 <= event.pos[1] <= 280:
                        print("Play")
                        game()
                    if 300 <= event.pos[0] <= 500 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        sys.exit()

def game():
    run = True
    
    global keys
    keys = {
        "right": False,
        "left": False,
        "up": False,
        "down": False
    }

    player = Player(400, 300, 50, 50)

    if dificuldade == 0:

        for i in range(3, 0, -1):
            screen.fill((0,0,0))
            alert = font.render("Dificuldade: Facil", True, white)
            screen.blit(alert, (300, 300))
            alert_seg = font.render("Segundos: 15", True, white)
            screen.blit(alert_seg, (300, 350))
            txt_alert = font.render(str(i), True, white)
            screen.blit(txt_alert, (400, 400))

            alert_sound = pygame.mixer.Sound("beep.wav")
            alert_sound.play()
            alert_sound.set_volume(0.1)
            pygame.display.update()
            time.sleep(1)

        enemy = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy1 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy2 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)

        timer = 900 # 15 segundos

        run = True
        while run:

            timer -= 1
            print(timer)
            
            if timer == 0:
                screen.fill((0, 0, 0))
                alert = font.render("Você perdeu!", True, white)
                screen.blit(alert, (300, 300))
                pygame.display.update()
                time.sleep(3)
                death()


            clock.tick(fps)
            screen.fill((0, 0, 0))

            if timer >= 840 and timer <= 900:
                alert = font.render("15s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 780 and timer <= 840:
                alert = font.render("14s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 720 and timer <= 780:
                alert = font.render("13s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 660 and timer <= 720:
                alert = font.render("12s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 600 and timer <= 660:
                alert = font.render("11s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 540 and timer <= 600:
                alert = font.render("10s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 480 and timer <= 540:
                alert = font.render("9s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 420 and timer <= 480:
                alert = font.render("8s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 360 and timer <= 420:
                alert = font.render("7s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 300 and timer <= 360:
                alert = font.render("6s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 240 and timer <= 300:
                alert = font.render("5s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 180 and timer <= 240:
                alert = font.render("4s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 120 and timer <= 180:
                alert = font.render("3s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 60 and timer <= 120:
                alert = font.render("2s", True, white)
                screen.blit(alert, (50, 50))
            if timer >= 0 and timer <= 60:
                alert = font.render("1s", True, white)
                screen.blit(alert, (50, 50))

            # timer_display = font.render(str(timer), True, white)
            # screen.blit(timer_display, (50, 50))

            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            all_sprites.add(enemy)
            all_sprites.add(enemy1)
            all_sprites.add(enemy2)

            all_sprites.update()
            all_sprites.draw(screen)

            enemy.Enemy_move(player.rect)
            enemy1.Enemy_move(player.rect)
            enemy2.Enemy_move(player.rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu()

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        keys["right"] = True
                    elif event.key == pygame.K_a:
                        keys["left"] = True
                    elif event.key == pygame.K_w:
                        keys["up"] = True
                    elif event.key == pygame.K_s:
                        keys["down"] = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        keys["right"] = False
                    elif event.key == pygame.K_a:
                        keys["left"] = False
                    elif event.key == pygame.K_w:
                        keys["up"] = False
                    elif event.key == pygame.K_s:
                        keys["down"] = False

            if keys["right"]:
                player.update()
            if keys["left"]:
                player.update()
            if keys["up"]:
                player.update()
            if keys["down"]:
                player.update()

            if player.rect.colliderect(enemy.rect):
                death()
            if player.rect.colliderect(enemy1.rect):
                death()
            if player.rect.colliderect(enemy2.rect):
                death()

            if enemy.rect.colliderect(enemy1.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy2.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy1.rect.colliderect(enemy2.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            pygame.display.update()

    elif dificuldade == 1:

        for i in range(3, 0, -1):
            screen.fill((0,0,0))
            alert = font.render("Dificuldade: Média", True, white)
            screen.blit(alert, (300, 300))
            alert_seg = font.render("Segundos: 30", True, white)
            screen.blit(alert_seg, (300, 350))
            txt_alert = font.render(str(i), True, white)
            screen.blit(txt_alert, (400, 400))

            alert_sound = pygame.mixer.Sound("beep.wav")
            alert_sound.play()
            alert_sound.set_volume(0.1)
            pygame.display.update()
            time.sleep(1)

        enemy = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy1 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy2 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy3 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy4 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy5 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)

        timer = 1800 # 30 segundos

        while run:
                
                clock.tick(fps)
                screen.fill((0, 0, 0))

                timer -= 1
                print(timer)

                if timer == 0:
                    screen.fill((0, 0, 0))
                    alert = font.render("Você perdeu!", True, white)
                    screen.blit(alert, (300, 300))
                    pygame.display.update()
                    time.sleep(3)
                    death()
    
                all_sprites = pygame.sprite.Group()
                all_sprites.add(player)
                all_sprites.add(enemy)
                all_sprites.add(enemy1)
                all_sprites.add(enemy2)
                all_sprites.add(enemy3)
                all_sprites.add(enemy4)
                all_sprites.add(enemy5)
    
                all_sprites.update()
                all_sprites.draw(screen)
    
                enemy.Enemy_move(player.rect)
                enemy1.Enemy_move(player.rect)
                enemy2.Enemy_move(player.rect)
                enemy3.Enemy_move(player.rect)
                enemy4.Enemy_move(player.rect)
                enemy5.Enemy_move(player.rect)
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            menu()
    
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            keys["right"] = True
                        elif event.key == pygame.K_a:
                            keys["left"] = True
                        elif event.key == pygame.K_w:
                            keys["up"] = True
                        elif event.key == pygame.K_s:
                            keys["down"] = True
    
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            keys["right"] = False
                        elif event.key == pygame.K_a:
                            keys["left"] = False
                        elif event.key == pygame.K_w:
                            keys["up"] = False
                        elif event.key == pygame.K_s:
                            keys["down"] = False
    
                if keys["right"]:
                    player.update()
                if keys["left"]:
                    player.update()
                if keys["up"]:
                    player.update()
                if keys["down"]:
                    player.update()
    
                if player.rect.colliderect(enemy.rect):
                    death()
                if player.rect.colliderect(enemy1.rect):
                    death()
                if player.rect.colliderect(enemy2.rect):
                    death()
                if player.rect.colliderect(enemy3.rect):
                    death()
                if player.rect.colliderect(enemy4.rect):
                    death()
                if player.rect.colliderect(enemy5.rect):
                    death()
    
                if enemy.rect.colliderect(enemy1.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1
    
                if enemy.rect.colliderect(enemy2.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1

                if enemy.rect.colliderect(enemy3.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1

                if enemy.rect.colliderect(enemy4.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1

                if enemy.rect.colliderect(enemy5.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1

                if enemy1.rect.colliderect(enemy2.rect):
                    enemy1.rect.x = enemy1.rect.x + 1
                    enemy1.rect.y = enemy1.rect.y + 1

                if enemy1.rect.colliderect(enemy3.rect):
                    enemy1.rect.x = enemy1.rect.x + 1
                    enemy1.rect.y = enemy1.rect.y + 1

                if enemy1.rect.colliderect(enemy4.rect):
                    enemy1.rect.x = enemy1.rect.x + 1
                    enemy1.rect.y = enemy1.rect.y + 1

                if enemy1.rect.colliderect(enemy5.rect):
                    enemy1.rect.x = enemy1.rect.x + 1
                    enemy1.rect.y = enemy1.rect.y + 1

                if enemy2.rect.colliderect(enemy3.rect):
                    enemy2.rect.x = enemy2.rect.x + 1
                    enemy2.rect.y = enemy2.rect.y + 1

                if enemy2.rect.colliderect(enemy4.rect):
                    enemy2.rect.x = enemy2.rect.x + 1
                    enemy2.rect.y = enemy2.rect.y + 1

                if enemy2.rect.colliderect(enemy5.rect):
                    enemy2.rect.x = enemy2.rect.x + 1
                    enemy2.rect.y = enemy2.rect.y + 1

                if enemy3.rect.colliderect(enemy4.rect):
                    enemy3.rect.x = enemy3.rect.x + 1
                    enemy3.rect.y = enemy3.rect.y + 1

                if enemy3.rect.colliderect(enemy5.rect):
                    enemy3.rect.x = enemy3.rect.x + 1
                    enemy3.rect.y = enemy3.rect.y + 1

                if enemy4.rect.colliderect(enemy5.rect):
                    enemy4.rect.x = enemy4.rect.x + 1
                    enemy4.rect.y = enemy4.rect.y + 1

                pygame.display.update()
                clock.tick(144)

    elif dificuldade == 2:

        for i in range(3, 0, -1):
            screen.fill((0,0,0))
            alert = font.render("Dificuldade: Dificíl", True, white)
            screen.blit(alert, (300, 300))
            alert_seg = font.render("Segundos: 45", True, white)
            screen.blit(alert_seg, (300, 350))
            txt_alert = font.render(str(i), True, white)
            screen.blit(txt_alert, (400, 400))

            alert_sound = pygame.mixer.Sound("beep.wav")
            alert_sound.play()
            alert_sound.set_volume(0.1)
            pygame.display.update()
            time.sleep(1)

        enemy = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy1 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy2 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy3 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy4 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy5 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy6 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy7 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy8 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy9 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy10 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)

        timer = 2700 # 45 segundos

        while True:

            clock.tick(fps)
            screen.fill((0, 0, 0))

            timer -= 1
            print(timer)

            if timer == 0:
                screen.fill((0, 0, 0))
                alert = font.render("Você perdeu!", True, white)
                screen.blit(alert, (300, 300))
                pygame.display.update()
                time.sleep(3)
                death()

            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            all_sprites.add(enemy)
            all_sprites.add(enemy1)
            all_sprites.add(enemy2)
            all_sprites.add(enemy3)
            all_sprites.add(enemy4)
            all_sprites.add(enemy5)
            all_sprites.add(enemy6)
            all_sprites.add(enemy7)
            all_sprites.add(enemy8)
            all_sprites.add(enemy9)
            all_sprites.add(enemy10)

            all_sprites.update()
            all_sprites.draw(screen)

            enemy.Enemy_move(player.rect)
            enemy1.Enemy_move(player.rect)
            enemy2.Enemy_move(player.rect)
            enemy3.Enemy_move(player.rect)
            enemy4.Enemy_move(player.rect)
            enemy5.Enemy_move(player.rect)
            enemy6.Enemy_move(player.rect)
            enemy7.Enemy_move(player.rect)
            enemy8.Enemy_move(player.rect)
            enemy9.Enemy_move(player.rect)
            enemy10.Enemy_move(player.rect)

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            menu()
    
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            keys["right"] = True
                        elif event.key == pygame.K_a:
                            keys["left"] = True
                        elif event.key == pygame.K_w:
                            keys["up"] = True
                        elif event.key == pygame.K_s:
                            keys["down"] = True
    
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            keys["right"] = False
                        elif event.key == pygame.K_a:
                            keys["left"] = False
                        elif event.key == pygame.K_w:
                            keys["up"] = False
                        elif event.key == pygame.K_s:
                            keys["down"] = False
    
            if keys["right"]:
                player.update()
            if keys["left"]:
                player.update()
            if keys["up"]:
                player.update()
            if keys["down"]:
                player.update()
    
            if player.rect.colliderect(enemy.rect):
                death()
            if player.rect.colliderect(enemy1.rect):
                death()
            if player.rect.colliderect(enemy2.rect):
                death()
            if player.rect.colliderect(enemy3.rect):
                death()
            if player.rect.colliderect(enemy4.rect):
                death()
            if player.rect.colliderect(enemy5.rect):
                death()
            if player.rect.colliderect(enemy6.rect):
                death()
            if player.rect.colliderect(enemy7.rect):
                death()
            if player.rect.colliderect(enemy8.rect):
                death()
            if player.rect.colliderect(enemy9.rect):
                death()
            if player.rect.colliderect(enemy10.rect):
                death()
    
            if enemy.rect.colliderect(enemy1.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1
    
            if enemy.rect.colliderect(enemy2.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy3.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy4.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy5.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy1.rect.colliderect(enemy2.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy3.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy4.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy5.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy2.rect.colliderect(enemy3.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy2.rect.colliderect(enemy4.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy2.rect.colliderect(enemy5.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy3.rect.colliderect(enemy4.rect):
                enemy3.rect.x = enemy3.rect.x + 1
                enemy3.rect.y = enemy3.rect.y + 1

            if enemy3.rect.colliderect(enemy5.rect):
                enemy3.rect.x = enemy3.rect.x + 1
                enemy3.rect.y = enemy3.rect.y + 1

            if enemy4.rect.colliderect(enemy5.rect):
                enemy4.rect.x = enemy4.rect.x + 1
                enemy4.rect.y = enemy4.rect.y + 1

            if enemy5.rect.colliderect(enemy6.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy7.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy8.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy9.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy10.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy6.rect.colliderect(enemy7.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy6.rect.colliderect(enemy8.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy6.rect.colliderect(enemy9.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1   

            if enemy6.rect.colliderect(enemy10.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy7.rect.colliderect(enemy8.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1

            if enemy7.rect.colliderect(enemy9.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1

            if enemy7.rect.colliderect(enemy10.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1   

            if enemy8.rect.colliderect(enemy9.rect):
                enemy8.rect.x = enemy8.rect.x + 1
                enemy8.rect.y = enemy8.rect.y + 1
                
            if enemy8.rect.colliderect(enemy10.rect):
                enemy8.rect.x = enemy8.rect.x + 1
                enemy8.rect.y = enemy8.rect.y + 1

            if enemy9.rect.colliderect(enemy10.rect):
                enemy9.rect.x = enemy9.rect.x + 1
                enemy9.rect.y = enemy9.rect.y + 1

            pygame.display.update()
            clock.tick(300)

    elif dificuldade == 3:

        for i in range(3, 0, -1):
            screen.fill((0,0,0))
            alert = font.render("Dificuldade: Ultra", True, white)
            screen.blit(alert, (300, 300))
            alert_seg = font.render("Segundos: 15", True, white)
            screen.blit(alert_seg, (300, 350))
            txt_alert = font.render(str(i), True, white)
            screen.blit(txt_alert, (400, 400))

            alert_sound = pygame.mixer.Sound("beep.wav")
            alert_sound.play()
            alert_sound.set_volume(0.1)
            pygame.display.update()
            time.sleep(1)

        enemy = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy1 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy2 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy3 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy4 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy5 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy6 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy7 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy8 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy9 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy10 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy11 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy12 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy13 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy14 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)
        enemy15 = Enemy(random.randint(0, 800), random.randint(0, 600), 50, 50)

        timer = 900 # 15 segundos

        while True:

            clock.tick(fps)
            screen.fill((0, 0, 0))

            timer -= 1

            if timer == 0:
                screen.fill((0, 0, 0))
                alert = font.render("Você perdeu!", True, white)
                screen.blit(alert, (300, 300))
                pygame.display.update()
                time.sleep(3)
                break

            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            all_sprites.add(enemy)
            all_sprites.add(enemy1)
            all_sprites.add(enemy2)
            all_sprites.add(enemy3)
            all_sprites.add(enemy4)
            all_sprites.add(enemy5)
            all_sprites.add(enemy6)
            all_sprites.add(enemy7)
            all_sprites.add(enemy8)
            all_sprites.add(enemy9)
            all_sprites.add(enemy10)
            all_sprites.add(enemy11)
            all_sprites.add(enemy12)
            all_sprites.add(enemy13)
            all_sprites.add(enemy14)
            all_sprites.add(enemy15)

            all_sprites.update()
            all_sprites.draw(screen)

            enemy.Enemy_move(player.rect)
            enemy1.Enemy_move(player.rect)
            enemy2.Enemy_move(player.rect)
            enemy3.Enemy_move(player.rect)
            enemy4.Enemy_move(player.rect)
            enemy5.Enemy_move(player.rect)
            enemy6.Enemy_move(player.rect)
            enemy7.Enemy_move(player.rect)
            enemy8.Enemy_move(player.rect)
            enemy9.Enemy_move(player.rect)
            enemy10.Enemy_move(player.rect)
            enemy11.Enemy_move(player.rect)
            enemy12.Enemy_move(player.rect)
            enemy13.Enemy_move(player.rect)
            enemy14.Enemy_move(player.rect)
            enemy15.Enemy_move(player.rect)

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            menu()
    
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            keys["right"] = True
                        elif event.key == pygame.K_a:
                            keys["left"] = True
                        elif event.key == pygame.K_w:
                            keys["up"] = True
                        elif event.key == pygame.K_s:
                            keys["down"] = True
    
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            keys["right"] = False
                        elif event.key == pygame.K_a:
                            keys["left"] = False
                        elif event.key == pygame.K_w:
                            keys["up"] = False
                        elif event.key == pygame.K_s:
                            keys["down"] = False
    
            if keys["right"]:
                player.update()
            if keys["left"]:
                player.update()
            if keys["up"]:
                player.update()
            if keys["down"]:
                player.update()
    
            if player.rect.colliderect(enemy.rect):
                death()
            if player.rect.colliderect(enemy1.rect):
                death()
            if player.rect.colliderect(enemy2.rect):
                death()
            if player.rect.colliderect(enemy3.rect):
                death()
            if player.rect.colliderect(enemy4.rect):
                death()
            if player.rect.colliderect(enemy5.rect):
                death()
            if player.rect.colliderect(enemy6.rect):
                death()
            if player.rect.colliderect(enemy7.rect):
                death()
            if player.rect.colliderect(enemy8.rect):
                death()
            if player.rect.colliderect(enemy9.rect):
                death()
            if player.rect.colliderect(enemy10.rect):
                death()
            if player.rect.colliderect(enemy11.rect):
                death()
            if player.rect.colliderect(enemy12.rect):
                death()
            if player.rect.colliderect(enemy13.rect):
                death()
            if player.rect.colliderect(enemy14.rect):
                death()
            if player.rect.colliderect(enemy15.rect):
                death()
    
            if enemy.rect.colliderect(enemy1.rect):
                    enemy.rect.x = enemy.rect.x + 1
                    enemy.rect.y = enemy.rect.y + 1
    
            if enemy.rect.colliderect(enemy2.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy3.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy4.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy.rect.colliderect(enemy5.rect):
                enemy.rect.x = enemy.rect.x + 1
                enemy.rect.y = enemy.rect.y + 1

            if enemy1.rect.colliderect(enemy2.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy3.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy4.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy1.rect.colliderect(enemy5.rect):
                enemy1.rect.x = enemy1.rect.x + 1
                enemy1.rect.y = enemy1.rect.y + 1

            if enemy2.rect.colliderect(enemy3.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy2.rect.colliderect(enemy4.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy2.rect.colliderect(enemy5.rect):
                enemy2.rect.x = enemy2.rect.x + 1
                enemy2.rect.y = enemy2.rect.y + 1

            if enemy3.rect.colliderect(enemy4.rect):
                enemy3.rect.x = enemy3.rect.x + 1
                enemy3.rect.y = enemy3.rect.y + 1

            if enemy3.rect.colliderect(enemy5.rect):
                enemy3.rect.x = enemy3.rect.x + 1
                enemy3.rect.y = enemy3.rect.y + 1

            if enemy4.rect.colliderect(enemy5.rect):
                enemy4.rect.x = enemy4.rect.x + 1
                enemy4.rect.y = enemy4.rect.y + 1

            if enemy5.rect.colliderect(enemy6.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy7.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy8.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy9.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy5.rect.colliderect(enemy10.rect):
                enemy5.rect.x = enemy5.rect.x + 1
                enemy5.rect.y = enemy5.rect.y + 1

            if enemy6.rect.colliderect(enemy7.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy6.rect.colliderect(enemy8.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy6.rect.colliderect(enemy9.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1   

            if enemy6.rect.colliderect(enemy10.rect):
                enemy6.rect.x = enemy6.rect.x + 1
                enemy6.rect.y = enemy6.rect.y + 1

            if enemy7.rect.colliderect(enemy8.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1

            if enemy7.rect.colliderect(enemy9.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1

            if enemy7.rect.colliderect(enemy10.rect):
                enemy7.rect.x = enemy7.rect.x + 1
                enemy7.rect.y = enemy7.rect.y + 1   

            if enemy8.rect.colliderect(enemy9.rect):
                enemy8.rect.x = enemy8.rect.x + 1
                enemy8.rect.y = enemy8.rect.y + 1
                
            if enemy8.rect.colliderect(enemy10.rect):
                enemy8.rect.x = enemy8.rect.x + 1
                enemy8.rect.y = enemy8.rect.y + 1

            if enemy9.rect.colliderect(enemy10.rect):
                enemy9.rect.x = enemy9.rect.x + 1
                enemy9.rect.y = enemy9.rect.y + 1

            if enemy10.rect.colliderect(enemy11.rect):
                enemy10.rect.x = enemy10.rect.x + 1
                enemy10.rect.y = enemy10.rect.y + 1

            if enemy10.rect.colliderect(enemy12.rect):
                enemy10.rect.x = enemy10.rect.x + 1
                enemy10.rect.y = enemy10.rect.y + 1

            if enemy10.rect.colliderect(enemy13.rect):
                enemy10.rect.x = enemy10.rect.x + 1
                enemy10.rect.y = enemy10.rect.y + 1

            if enemy10.rect.colliderect(enemy14.rect):
                enemy10.rect.x = enemy10.rect.x + 1
                enemy10.rect.y = enemy10.rect.y + 1

            if enemy10.rect.colliderect(enemy15.rect):
                enemy10.rect.x = enemy10.rect.x + 1
                enemy10.rect.y = enemy10.rect.y + 1

            if enemy11.rect.colliderect(enemy12.rect):
                enemy11.rect.x = enemy11.rect.x + 1
                enemy11.rect.y = enemy11.rect.y + 1

            if enemy11.rect.colliderect(enemy13.rect):
                enemy11.rect.x = enemy11.rect.x + 1
                enemy11.rect.y = enemy11.rect.y + 1

            if enemy11.rect.colliderect(enemy14.rect):
                enemy11.rect.x = enemy11.rect.x + 1
                enemy11.rect.y = enemy11.rect.y + 1

            if enemy11.rect.colliderect(enemy15.rect):
                enemy11.rect.x = enemy11.rect.x + 1
                enemy11.rect.y = enemy11.rect.y + 1

            if enemy12.rect.colliderect(enemy13.rect):
                enemy12.rect.x = enemy12.rect.x + 1
                enemy12.rect.y = enemy12.rect.y + 1

            if enemy12.rect.colliderect(enemy14.rect):
                enemy12.rect.x = enemy12.rect.x + 1
                enemy12.rect.y = enemy12.rect.y + 1

            if enemy12.rect.colliderect(enemy15.rect):
                enemy12.rect.x = enemy12.rect.x + 1
                enemy12.rect.y = enemy12.rect.y + 1

            if enemy13.rect.colliderect(enemy14.rect):
                enemy13.rect.x = enemy13.rect.x + 1
                enemy13.rect.y = enemy13.rect.y + 1

            if enemy13.rect.colliderect(enemy15.rect):
                enemy13.rect.x = enemy13.rect.x + 1
                enemy13.rect.y = enemy13.rect.y + 1

            if enemy14.rect.colliderect(enemy15.rect):
                enemy14.rect.x = enemy14.rect.x + 1
                enemy14.rect.y = enemy14.rect.y + 1

            pygame.display.update()
            clock.tick(300)

def main():
    run = True
    while run:

        clock.tick(fps)

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, red, (300, 300, 200, 50))
        text = font.render("Quit", True, black)
        screen.blit(text, (370, 305))

        pygame.draw.rect(screen, green, (300, 230, 200, 50))
        text = font.render("Play", True, black)
        screen.blit(text, (370, 235))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 <= event.pos[0] <= 500 and 230 <= event.pos[1] <= 280:
                        print("Play")
                        game()
                    if 300 <= event.pos[0] <= 500 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
