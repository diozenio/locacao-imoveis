from utils.divider import divider
from utils.generate_id import generate_id

def register():
    divider()
    name = input("Digite o seu nome: ")
    username = input("Digite o seu username: ")
    password = input("Digite a sua senha: ")
    divider()
    user = {"user_id": generate_id(), "name": name, "username": username, "password": password}
    return user

def login():
    divider()
    username = input("Digite o seu username: ")
    password = input("Digite a sua senha: ")
    divider()
    return {"username": username, "password": password}

    