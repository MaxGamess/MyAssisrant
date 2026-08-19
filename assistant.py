from time import *
from random import *
from sys import *

request = ""
socket = ""

def variating(socket):
    request_fix = request.lower()
    for word in {"привет", "хай", "здарова", "ку", "старт", "салам"}:
        if word in request_fix:
            return greeting(request_fix)
    for word in {"пока", "алибидерчи", "бб", "стоп"}:
        if word in request_fix:
            return farewell(request_fix)

def greeting(socket):
    def_sct = "Приветствую вас"
    sct = ""
    rnd = randint(0,2)
    if rnd == 0:
        sct = def_sct + ", сэр!"
    elif rnd == 1:
        sct = "Добро пожаловать!"
    else:
        sct = def_sct + "!"
    return sct

def farewell(socket):
    def_sct = "До свиданнья"
    sct = ""
    rnd = randint(0,2)
    if rnd == 0:
        sct = def_sct + ", сэр!"
        print(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
        exit()
    elif rnd == 1:
        sct = "До следующего сеанса!"
        print(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
        exit()
    else:
        sct = def_sct + "!"
        print(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
    return exit()

while True:
    request = input(">>> ")
    socket = variating(request)
    print(socket)
