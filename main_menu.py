import os
import sys
import time
import tkinter as ttk
import json
import subprocess
import pygame
import random
import math
import pygame.mixer
from pygame.locals import *
import json

JsonFile = open("contas.json")
JsonData = json.load(JsonFile)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

tempo = 0
budcoin = 0

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        self.master.geometry("405x110")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = ttk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = ttk.Label(self.frame, text="Main Menu", font=("Arial", 20))
        self.title.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.button1 = ttk.Button(self.frame, text="Register", font=("Arial"), command=self.register)
        self.button1.grid(row=1, column=0, pady=10, padx=10)
        self.button1.config(width=8, bg="lightblue", cursor="hand2")

        self.button2 = ttk.Button(self.frame, text="Login", font=("Arial"), command=self.login)
        self.button2.grid(row=1, column=1, pady=10, padx=60)
        self.button2.config(width=8, bg="lightblue", cursor="hand2")

        self.button3 = ttk.Button(self.frame, text="Sair", font=("Arial"), command=self.sair)
        self.button3.grid(row=1, column=3, padx=10)
        self.button3.config(width=8, bg="lightblue", cursor="hand2")


    def register(self):
        self.master.destroy()
        self.master = ttk.Tk()
        self.master.title("Register")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = ttk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = ttk.Label(self.frame, text="Regista-te!", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.name_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.name_entry.config(width=30)

        self.name_label = ttk.Label(self.frame, text="Nome", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)
        self.name_label.config(bg="lightblue")

        self.school_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.school_entry.grid(row=2, column=1, pady=10, padx=10)
        self.school_entry.config(width=30)

        self.school_label = ttk.Label(self.frame, text="Escola", font=("Arial", 12))
        self.school_label.grid(row=2, column=0, pady=10, padx=10)
        self.school_label.config(bg="lightblue")

        self.password_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10)
        self.password_entry.config(width=30, show="*")

        self.password_label = ttk.Label(self.frame, text="Senha", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, pady=10, padx=10)
        self.password_label.config(bg="lightblue")

        self.seepass_button = ttk.Button(self.frame, text="Ver", font=("Arial", 10), command=self.see_password)
        self.seepass_button.grid(row=3, column=2)
        self.seepass_button.config(width=5, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.login_button = ttk.Button(self.frame, text="Já tem uma conta?", font=("Arial", 10), command=self.login)
        self.login_button.grid(row=4, column=1)
        self.login_button.config(width=20, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.register_button = ttk.Button(self.frame, text="Registar", font=("Arial", 10), command=self.RegisterToJson)
        self.register_button.grid(row=4, column=0)
        self.register_button.config(width=8, bg="lightblue", cursor="hand2")

    def RegisterToJson(self):
        name = self.name_entry.get()
        school = self.school_entry.get()
        password = self.password_entry.get()

        if name == "" or school == "" or password == "":
            self.label_error = ttk.Label(self.frame, text="Preencha todos os campos!", font=("Arial", 10))
            self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
            self.label_error.config(bg="lightblue", fg="red")
        else:
            with open("contas.json", "r") as file:
                data = json.load(file)
                data.append({
                    "name": name,
                    "school": school,
                    "password": password,
                    "budcoins": 0,
                    "velocidade": 0,
                    "dificuldade": 0
                })
            with open("contas.json", "w") as file:
                json.dump(data, file, indent=4)
            self.label_created = ttk.Label(self.frame, text="Conta criada com sucesso!", font=("Arial", 10))
            self.label_created.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
            self.label_created.config(bg="lightblue", fg="green")

    def see_password(self):
        if self.password_entry["show"] == "*":
            self.password_entry["show"] = ""
            self.seepass_button["text"] = "Ocultar"
        else:
            self.password_entry["show"] = "*"
            self.seepass_button["text"] = "Ver"

    def login(self):
        self.master.destroy()
        self.master = ttk.Tk()
        self.master.title("Login")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = ttk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = ttk.Label(self.frame, text="Login", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=10, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.name_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.name_entry.config(width=30)

        self.name_label = ttk.Label(self.frame, text="Nome", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)
        self.name_label.config(bg="lightblue")

        self.password_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10)
        self.password_entry.config(width=30, show="*")

        self.password_label = ttk.Label(self.frame, text="Senha", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, pady=10, padx=10)
        self.password_label.config(bg="lightblue")

        self.seepass_button = ttk.Button(self.frame, text="Ver", font=("Arial", 10), command=self.see_password)
        self.seepass_button.grid(row=3, column=2)
        self.seepass_button.config(width=5, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.login_button = ttk.Button(self.frame, text="Login", font=("Arial", 10), command=self.VerifyLogin)
        self.login_button.grid(row=4, column=0)
        self.login_button.config(width=8, bg="lightblue", cursor="hand2")

        self.register_button = ttk.Button(self.frame, text="Registar", font=("Arial", 10), command=self.register)
        self.register_button.grid(row=4, column=1)
        self.register_button.config(width=8, bg="lightblue", cursor="hand2")

    def VerifyLogin(self):
        name = self.name_entry.get()
        password = self.password_entry.get()

        with open("contas.json", "r") as file:
            data = json.load(file)
            for i in data:
                print(i["name"], i["password"])
                if name == i["name"] and password == i["password"]:
                    
                    global NAMELOGGED, PASSLOGGED
                    NAMELOGGED = i["name"]
                    PASSLOGGED = i["password"]


                    self.master.destroy()
                    self.principal()

                if name != i["name"] or password != i["password"]:
                    self.label_error = ttk.Label(self.frame, text="Nome ou senha incorretos!", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

                if name == "" or password == "":
                    self.label_error = ttk.Label(self.frame, text="Preencha todos os campos", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

    def principal(self):
        self.master = ttk.Tk()
        self.master.title("Menu Principal")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame_master = ttk.Frame(self.master)
        self.frame_master.config(bg="lightblue")
        self.frame_master.pack()

        self.title = ttk.Label(self.frame_master, text="Menu Principal", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=10, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.sair_button = ttk.Button(self.frame_master, text="Sair", font=("Arial", 10), command=self.sair)
        self.sair_button.grid(row=4, column=0)
        self.sair_button.config(width=8, bg="lightblue", cursor="hand2")

        self.play_button = ttk.Button(self.frame_master, text="Jogar", font=("Arial", 10), command=self.jogar)
        self.play_button.grid(row=4, column=1)
        self.play_button.config(width=8, bg="lightblue", cursor="hand2")

    def jogar(self):
        self.master.iconify()
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # Tamanho da tela

        screen = pygame.display.set_mode((800, 600))
        screen.fill((0, 0, 0))
        pygame.display.set_caption("1 vs 100")

        # Variáveis

        global backmusic
        backmusic = pygame.mixer.Sound("backmusic2.wav")
        backmusic.play(loops=-1)
        backmusic.set_volume(0.1)

        clock = pygame.time.Clock()
        fps = 60
        font = pygame.font.SysFont("Arial", 30)

        # Cores

        # Imagens

        ## Por enquanto não tem

        # Sons

        ## Por enquanto não tem

        # Classes

        def menu():
            run = True

            with open("contas.json", "r") as file:
                data = json.load(file)
                for i in data:
                    if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                        global budcoins
                        budcoins = i["budcoins"]

            while run:
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, red, (300, 300, 200, 50))
                text = font.render("Sair", True, black)
                screen.blit(text, (370, 305))

                pygame.draw.rect(screen, green, (300, 230, 200, 50))
                text = font.render("Continuar", True, black)
                screen.blit(text, (335, 235))

                if budcoins > 15:
                    pygame.draw.rect(screen, blue, (440, 530, 320, 50))
                    text = font.render("Velocidade (15 Coins)", True, black)
                    screen.blit(text, (452, 540))
                else:
                    pygame.draw.rect(screen, red, (440, 530, 320, 50))
                    text = font.render("Velocidade (15 Coins)", True, black)
                    screen.blit(text, (452, 540))

                if budcoins >= 20:
                    pygame.draw.rect(screen, blue, (30, 530, 320, 50))
                    text = font.render("Dificuldade (20 Coins)", True, black)
                    screen.blit(text, (42, 540))
                else:
                    pygame.draw.rect(screen, red, (30, 530, 320, 50))
                    text = font.render("Dificuldade (20 Coins)", True, black)
                    screen.blit(text, (42, 540))

                text = font.render("Budcoins: " + str(budcoins), True, white)
                screen.blit(text, (10, 10))

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
                                if budcoins >= 20:
                                    global dificuldade
                                    dificuldade += 1
                                    with open("contas.json", "r") as file:
                                        data = json.load(file)
                                        for i in data:
                                            if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                                i["budcoins"] -= 20
                                                i["dificuldade"] += 1
                                                with open("contas.json", "w") as file:
                                                    json.dump(data, file, indent=4)

                            if 300 <= event.pos[0] <= 500 and 530 <= event.pos[1] <= 580:
                                if budcoins >= 15:
                                    global velocidade
                                    with open("contas.json", "r") as file:
                                        data = json.load(file)
                                        for i in data:
                                            if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                                i["budcoins"] -= 15
                                                i["velocidade"] += 1
                                                with open("contas.json", "w") as file:
                                                    json.dump(data, file, indent=4)

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
                with open("contas.json", "r") as file:
                    data = json.load(file)
                    for i in data:
                        if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                            global velocidade
                            velocidade = i["velocidade"]

                if velocidade == 0:
                    if keys["right"]:
                        self.rect.x += 1
                    if keys["left"]:
                        self.rect.x -= 1
                    if keys["up"]:
                        self.rect.y -= 1
                    if keys["down"]:
                        self.rect.y += 1
                if velocidade == 1:
                    if keys["right"]:
                        self.rect.x += 2
                    if keys["left"]:
                        self.rect.x -= 2
                    if keys["up"]:
                        self.rect.y -= 2
                    if keys["down"]:
                        self.rect.y += 2
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

        def win():
            run = True

            with open("contas.json", "r") as file:
                data = json.load(file)
                for i in data:
                    if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                        global budcoins
                        budcoins = i["budcoins"]

            while run:
                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, red, (300, 300, 200, 50))
                text = font.render("Sair", True, black)
                screen.blit(text, (370, 305))

                pygame.draw.rect(screen, green, (300, 230, 200, 50))
                text = font.render("Continuar", True, black)
                screen.blit(text, (335, 235))

                if budcoins > 15:
                    pygame.draw.rect(screen, blue, (440, 530, 320, 50))
                    text = font.render("Velocidade (15 Coins)", True, black)
                    screen.blit(text, (452, 540))
                else:
                    pygame.draw.rect(screen, red, (440, 530, 320, 50))
                    text = font.render("Velocidade (15 Coins)", True, black)
                    screen.blit(text, (452, 540))

                if budcoins >= 20:
                    pygame.draw.rect(screen, blue, (30, 530, 320, 50))
                    text = font.render("Dificuldade (20 Coins)", True, black)
                    screen.blit(text, (42, 540))
                else:
                    pygame.draw.rect(screen, red, (30, 530, 320, 50))
                    text = font.render("Dificuldade (20 Coins)", True, black)
                    screen.blit(text, (42, 540))

                text = font.render("Budcoins: " + str(budcoins), True, white)
                screen.blit(text, (10, 10))

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

                            if 30 <= event.pos[0] <= 230 and 530 <= event.pos[1] <= 580:
                                if budcoins >= 20:
                                    with open("contas.json", "r") as file:
                                        data = json.load(file)
                                        for i in data:
                                            if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                                i["budcoins"] -= 20
                                                i["dificuldade"] += 1
                                                with open("contas.json", "w") as file:
                                                    json.dump(data, file, indent=4)

                            if 300 <= event.pos[0] <= 500 and 530 <= event.pos[1] <= 580:
                                if budcoins >= 15:
                                    with open("contas.json", "r") as file:
                                        data = json.load(file)
                                        for i in data:
                                            if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                                i["budcoins"] -= 15
                                                i["velocidade"] += 1
                                                with open("contas.json", "w") as file:
                                                    json.dump(data, file, indent=4)
                                        

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

            with open("contas.json", "r") as file:
                data = json.load(file)
                for i in data:
                    if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                        dificuldade = i["dificuldade"]

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
                        alert = font.render("Você ganhou!", True, white)
                        screen.blit(alert, (300, 300))
                        pygame.display.update()
                        time.sleep(3)
                        win()


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
                        if timer == 540:
                            with open("contas.json", "r") as file:
                                data = json.load(file)
                                for i in data:
                                    print(i["name"], i["password"])
                                    if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                        i["budcoins"] += 2
                                        print(i["budcoins"])
                                        with open("contas.json", "w") as file:
                                            json.dump(data, file, indent=4)
                                            print("Salvo com sucesso!")

                        alert_sound = pygame.mixer.Sound("beep.wav")
                        alert_sound.play()
                        alert_sound.set_volume(0.1)
                        receive_budcoin = font.render("+2 BudCoins ", True, white)
                        screen.blit(receive_budcoin, (10, 10))
                    if timer >= 480 and timer <= 540:
                        alert = font.render("9s", True, white)
                        screen.blit(alert, (50, 50))
                        receive_budcoin = font.render("+2 BudCoins ", True, black)
                        screen.blit(receive_budcoin, (10, 10))
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
                        if timer == 240:
                            with open("contas.json", "r") as file:
                                data = json.load(file)
                                for i in data:
                                    print(i["name"], i["password"])
                                    if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                                        i["budcoins"] += 2
                                        print(i["budcoins"])
                                        with open("contas.json", "w") as file:
                                            json.dump(data, file, indent=4)
                                            print("Salvo com sucesso!")

                        alert_sound = pygame.mixer.Sound("beep.wav")
                        alert_sound.play()
                        alert_sound.set_volume(0.1)
                        receive_budcoin = font.render("+2 BudCoins ", True, white)
                        screen.blit(receive_budcoin, (10, 10))
                    if timer >= 180 and timer <= 240:
                        alert = font.render("4s", True, white)
                        screen.blit(alert, (50, 50))
                        receive_budcoin = font.render("+2 BudCoins ", True, black)
                        screen.blit(receive_budcoin, (10, 10))
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

                # pygame.draw.rect(screen, green, (100, 100, 200, 50))
                # text = font.render("Mute", True, black)
                # screen.blit(text, (100, 100))
                
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
                            # if 100 <= event.pos[0] <= 300 and 100 <= event.pos[1] <= 150:
                            #     print("Mute")


                pygame.display.update()

            pygame.quit()

        main()

    def sair(self):
        self.master.destroy()

def main_exec():
    root = ttk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main_exec()
