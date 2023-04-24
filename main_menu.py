import os
import sys
import time
import tkinter as ttk
import json
import subprocess

JsonFile = open("contas.json")
JsonData = json.load(JsonFile)

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
                    "password": password
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
                    self.master.destroy()
                    self.principal = ttk.Tk()
                    self.principal.title("Menu Principal")
                    self.principal.geometry("600x500")
                    self.principal.resizable(False, False)
                    self.principal.config(bg="lightblue")

                    self.frame_principal = ttk.Frame(self.principal)
                    self.frame_principal.config(bg="lightblue")
                    self.frame_principal.pack()

                    self.title = ttk.Label(self.frame_principal, text="Menu Principal", font=("Arial", 20))
                    self.title.grid(row=0, column=0, columnspan=10, pady=10, padx=10)
                    self.title.config(bg="lightblue")

                    self.sair_button = ttk.Button(self.frame_principal, text="Sair", font=("Arial", 10), command=self.__init__)
                    self.sair_button.grid(row=4, column=0)
                    self.sair_button.config(width=8, bg="lightblue", cursor="hand2")

                    self.play_button = ttk.Button(self.frame_principal, text="Jogar", font=("Arial", 10), command=self.jogar)
                    self.play_button.grid(row=4, column=1)
                    self.play_button.config(width=8, bg="lightblue", cursor="hand2")


                if name != i["name"] or password != i["password"]:
                    self.label_error = ttk.Label(self.frame, text="Nome ou senha incorretos!", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

                if name == "" or password == "":
                    self.label_error = ttk.Label(self.frame, text="Preencha todos os campos", font=("Arial", 10))
                    self.label_error.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
                    self.label_error.config(bg="lightblue", fg="red")

    def jogar(self):
        self.principal.iconify()
        subprocess.Popen(".bat", shell=True)


    def sair(self):
        self.master.destroy()

def main():
    root = ttk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()