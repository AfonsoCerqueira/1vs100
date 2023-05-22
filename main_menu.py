import os
import sys
import time
import tkinter as tk
from tkinter import ttk
import json
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
        self.master.title("Main Menu - Afonso")
        self.master.geometry("405x110")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = tk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = tk.Label(self.frame, text="Main Menu", font=("Arial", 20))
        self.title.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.button1 = tk.Button(self.frame, text="Register", font=("Arial"), command=self.register)
        self.button1.grid(row=1, column=0, pady=10, padx=10)
        self.button1.config(width=8, bg="lightblue", cursor="hand2")

        self.button2 = tk.Button(self.frame, text="Login", font=("Arial"), command=self.login)
        self.button2.grid(row=1, column=1, pady=10, padx=60)
        self.button2.config(width=8, bg="lightblue", cursor="hand2")

        self.button3 = tk.Button(self.frame, text="Sair", font=("Arial"), command=self.sair)
        self.button3.grid(row=1, column=3, padx=10)
        self.button3.config(width=8, bg="lightblue", cursor="hand2")


    def register(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.title("Register")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = tk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = tk.Label(self.frame, text="Regista-te!", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.name_entry.config(width=30)

        self.name_label = tk.Label(self.frame, text="Nome", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)
        self.name_label.config(bg="lightblue")

        self.school_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.school_entry.grid(row=2, column=1, pady=10, padx=10)
        self.school_entry.config(width=30)

        self.school_label = tk.Label(self.frame, text="Escola", font=("Arial", 12))
        self.school_label.grid(row=2, column=0, pady=10, padx=10)
        self.school_label.config(bg="lightblue")

        self.password_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10)
        self.password_entry.config(width=30, show="*")

        self.password_label = tk.Label(self.frame, text="Senha", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, pady=10, padx=10)
        self.password_label.config(bg="lightblue")

        self.seepass_button = tk.Button(self.frame, text="Ver", font=("Arial", 10), command=self.see_password)
        self.seepass_button.grid(row=3, column=2)
        self.seepass_button.config(width=5, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.login_button = tk.Button(self.frame, text="Já tem uma conta?", font=("Arial", 10), command=self.login)
        self.login_button.grid(row=4, column=1)
        self.login_button.config(width=20, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.register_button = tk.Button(self.frame, text="Registar", font=("Arial", 10), command=self.RegisterToJson)
        self.register_button.grid(row=4, column=0)
        self.register_button.config(width=8, bg="lightblue", cursor="hand2")

    def RegisterToJson(self):
        name = self.name_entry.get()
        school = self.school_entry.get()
        password = self.password_entry.get()

        if name == "" or school == "" or password == "":
            self.label_error = tk.Label(self.frame, text="Preencha todos os campos!", font=("Arial", 10))
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
                    "dificuldade": 0,
                    "permissao": 0
                })
            with open("contas.json", "w") as file:
                json.dump(data, file, indent=4)
            self.label_created = tk.Label(self.frame, text="Conta criada com sucesso!", font=("Arial", 10))
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
        self.master = tk.Tk()
        self.master.title("Login")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = tk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = tk.Label(self.frame, text="Login", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=10, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.name_entry.config(width=30)

        self.name_label = tk.Label(self.frame, text="Nome", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)
        self.name_label.config(bg="lightblue")

        self.password_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10)
        self.password_entry.config(width=30, show="*")

        self.password_label = tk.Label(self.frame, text="Senha", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, pady=10, padx=10)
        self.password_label.config(bg="lightblue")

        self.seepass_button = tk.Button(self.frame, text="Ver", font=("Arial", 10), command=self.see_password)
        self.seepass_button.grid(row=3, column=2)
        self.seepass_button.config(width=5, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

        self.login_button = tk.Button(self.frame, text="Login", font=("Arial", 10), command=self.VerifyLogin)
        self.login_button.grid(row=4, column=0)
        self.login_button.config(width=8, bg="lightblue", cursor="hand2")

        self.register_button = tk.Button(self.frame, text="Registar", font=("Arial", 10), command=self.register)
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
                    self.label_error = tk.Label(self.frame, text="Nome ou senha incorretos!", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

                if name == "" or password == "":
                    self.label_error = tk.Label(self.frame, text="Preencha todos os campos", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

    def principal(self):
        self.master = tk.Tk()
        self.master.title("Menu Principal")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame_master = tk.Frame(self.master)
        self.frame_master.config(bg="lightblue")
        self.frame_master.pack()

        self.title = tk.Label(self.frame_master, text="Menu Principal", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.play_button = tk.Button(self.frame_master, text="Jogar", font=("Arial", 10), command=self.jogar)
        self.play_button.grid(row=4, column=0, columnspan=5, pady=10, padx=10)
        self.play_button.config(width=8, bg="lightblue", cursor="hand2")

        with open("contas.json", "r") as file:
            data = json.load(file)
            for i in data:
                if NAMELOGGED == i["name"] and PASSLOGGED == i["password"]:
                    if i["permissao"] == 1:
                        self.admin_button = tk.Button(self.frame_master, text="Admin", font=("Arial", 10), command=self.adminmenu)
                        self.admin_button.grid(row=5, column=0, columnspan=5, pady=10, padx=10)
                        self.admin_button.config(width=8, bg="lightblue", cursor="hand2")
                        
                        self.sair_button = tk.Button(self.frame_master, text="Sair", font=("Arial", 10), command=self.sair)
                        self.sair_button.grid(row=6, column=0, columnspan=5, pady=10, padx=10)
                        self.sair_button.config(width=8, bg="lightblue", cursor="hand2")
                else:
                    self.sair_button = tk.Button(self.frame_master, text="Sair", font=("Arial", 10), command=self.sair)
                    self.sair_button.grid(row=6, column=0, columnspan=5, pady=10, padx=10)
                    self.sair_button.config(width=8, bg="lightblue", cursor="hand2")

    def adminmenu(self):
        self.master = tk.Tk()
        self.master.title("Admin Menu")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame_master = tk.Frame(self.master)
        self.frame_master.config(bg="lightblue")
        self.frame_master.pack()

        self.title = tk.Label(self.frame_master, text="Menu Admin", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.createacc_button = tk.Button(self.frame_master, text="Criar Conta", font=("Arial", 10), command=self.createadm)
        self.createacc_button.grid(row=1, column=1, columnspan=5, pady=10, padx=10)
        self.createacc_button.config(bg="lightblue")

        self.seeacc_button = tk.Button(self.frame_master, text="Contas", font=("Arial", 10), command=self.seeacc)
        self.seeacc_button.grid(row=2, column=0, columnspan=5, pady=5, padx=5)
        self.seeacc_button.config(bg="lightblue")

        self.sairadm_button = tk.Button(self.frame_master, text="Sair Admin", font=("Arial", 10), command=self.master.destroy)
        self.sairadm_button.grid(row=4, column=0, columnspan=5, pady=10, padx=10)
        self.sairadm_button.config(width=8, bg="lightblue", cursor="hand2")


    def createadm(self):
        self.master = tk.Tk()
        self.master.title("Register Admin")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame = tk.Frame(self.master)
        self.frame.config(bg="lightblue")
        self.frame.pack()

        self.title = tk.Label(self.frame, text="Criar Conta (Admin)", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.title.config(bg="lightblue")

        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10, padx=10)
        self.name_entry.config(width=30)

        self.name_label = tk.Label(self.frame, text="Nome", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)
        self.name_label.config(bg="lightblue")

        self.school_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.school_entry.grid(row=2, column=1, pady=10, padx=10)
        self.school_entry.config(width=30)

        self.school_label = tk.Label(self.frame, text="Escola", font=("Arial", 12))
        self.school_label.grid(row=2, column=0, pady=10, padx=10)
        self.school_label.config(bg="lightblue")

        self.password_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, pady=10, padx=10)
        self.password_entry.config(width=30, show="*")

        self.password_label = tk.Label(self.frame, text="Senha", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, pady=10, padx=10)
        self.password_label.config(bg="lightblue")

        self.permissao_label = tk.Label(self.frame, text="Permissão (0 = User // 1 = Admin)", font=("Arial", 9))
        self.permissao_label.grid(row=4, column=0, pady=10, padx=10)
        self.permissao_label.config(bg="lightblue")

        self.permissao_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.permissao_entry.grid(row=4, column=1, pady=10, padx=10)
        self.permissao_entry.config(width=30)

        self.send_button = tk.Button(self.frame, text="Enviar", font=("Arial", 10), command=self.RegisterToJsonAdm)
        self.send_button.grid(row=5, column=0)
        self.send_button.config(bg="lightblue")

        self.seepass_button = tk.Button(self.frame, text="Ver", font=("Arial", 10), command=self.see_password)
        self.seepass_button.grid(row=3, column=2)
        self.seepass_button.config(width=5, bg="lightblue", relief="flat", activebackground="lightblue", activeforeground="blue", bd=0, cursor="hand2", compound="center")

    def RegisterToJsonAdm(self):
            name = self.name_entry.get()
            school = self.school_entry.get()
            password = self.password_entry.get()
            permissao = self.permissao_entry.get()
            fnpermissao = int(permissao)
            print(fnpermissao)
            print(type(fnpermissao))

            if name == "" or school == "" or password == "" or permissao == "":
                self.label_error = tk.Label(self.frame, text="Preencha todos os campos!", font=("Arial", 10))
                self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                self.label_error.config(bg="lightblue", fg="red")

            if fnpermissao >= 2 or fnpermissao < 0:
                self.label_error = tk.Label(self.frame, text="Permissão Errada!", font=("Arial", 10))
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
                        "dificuldade": 0,
                        "permissao": fnpermissao
                    })
                with open("contas.json", "w") as file:
                    json.dump(data, file, indent=4)
                self.label_created = tk.Label(self.frame, text="Conta criada com sucesso!", font=("Arial", 10))
                self.label_created.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                self.label_created.config(bg="lightblue", fg="green")

    def seeacc(self):
        self.master = tk.Tk()
        self.master.title("Contas")
        self.master.geometry("800x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightblue")

        self.frame_master = tk.Frame(self.master)
        self.frame_master.config(bg="lightblue")
        self.frame_master.pack()

        self.acctext_label = tk.Label(self.frame_master, text="Contas", font=("Arial", 10))
        self.acctext_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.acctext_label.config(bg="lightblue")

        self.tree = ttk.Treeview(self.frame_master, columns=("Nome", "Password", "Permissão"))
        self.tree.heading("#0", text="Numeração")
        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="Password")
        self.tree.heading("#3", text="Permissão")
        self.tree.grid(row=4, column=0, columnspan=2)

        with open("contas.json", "r") as file:
            data = json.load(file)

        p = len(data)
        p += 1

        with open("contas.json", "r") as file:
            data = json.load(file)
            for i in reversed(data):
                p -= 1
                self.tree.insert("", 0, text=p, values=(i['name'], i['password'], i['permissao']))

        self.del_button = tk.Button(self.frame_master, text="Deletar Conta", font=("Arial", 10), command=self.deleteacc)
        self.del_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        self.del_button.config(bg="lightblue")

    def deleteacc(self):
        tree_selection = self.tree.selection()[-1]
        tree_selection_index = self.tree.index(tree_selection)
        self.tree.delete(tree_selection)

        print(tree_selection_index)
        
        with open("contas.json", "r") as file:
            data = json.load(file)
            data.pop(tree_selection_index)

        with open("contas.json", "w") as file:
            json.dump(data, file, indent=4)


    def jogar(self):
        self.master.destroy()
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

                pos1 = random.randint(0,800)
                pos2 = random.randint(0,600)
                pos3 = random.randint(0,800)
                pos4 = random.randint(0,600)
            

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
                        if player.rect.colliderect(pygame.draw.circle(screen, green, (pos1, pos2), 15, 4)):
                            if timer == 900:
                                pass
                            if timer < 900:
                                timer += 20    
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
                        if player.rect.colliderect(pygame.draw.circle(screen, green, (pos3, pos4), 15, 4)):
                            if timer == 900:
                                pass
                            if timer < 900:
                                timer = 900
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

#            elif dificuldade == 1:

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
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main_exec()