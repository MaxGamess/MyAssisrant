from time import *
from random import *
from sys import *

request = ""
socket = ""

def variating(socket):
    request_fix = request.lower()
    ultimate_words = {"привет", "хай", "здарова", "ку", "старт", "салам", "qq", "вернулся", "пока", "алибидерчи", "бб", "стоп", "калькулятор", "счет", "считать"}
    for word in {"привет", "хай", "здарова", "ку", "старт", "салам", "qq"}:
        if word in request_fix:
            return greeting(request_fix)
    for word in {"вернулся"}:
        if word in request_fix:
            return comeback(request_fix)
    for word in {"пока", "алибидерчи", "бб", "стоп"}:
        if word in request_fix:
            return farewell(request_fix)
    for word in {"калькулятор", "счет", "считать"}:
        if word in request_fix:
            rqst = ""
            result = calculator(rqst)
            if result == "вернулся":
                return comeback(result)
    for word in ultimate_words:
        if word not in request_fix:
            result = ""
            return default(result)

def default(socket):
    text = "Извините, но в моей базе не заготовлено ответа на данный вопрос"
    sct = ""
    rnd = randint(0,1)
    if rnd == 0:
        sct = text
    else:
        sct = "Простите, но у меня нет ответа на данный вопрос"
    return sct

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

def comeback(socket):
    def_sct = "С возвращением"
    sct = ""
    rnd = randint(0,1)
    if rnd == 0:
        sct = def_sct + ", сэр!"
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

def calculator(socket):
    operators = {"+", "-", "*", "/", "^"}
    rqst = ""
    
    while True:
        rqst = input("calc mod >>> ")
        
        fix_rqst = rqst.lower()
        cleaned = fix_rqst.replace(" ", "")
        word = set("0123456789+-*/^.")
        char = ""
        for char in cleaned:
            if char not in word:
                return "вернулся"
        
        numbers = []
        operators_list = []
        current_num = ""
        
        for char in cleaned:
            if char.isdigit() or char == '.':
                current_num += char
            elif char in operators:
                if current_num:
                    numbers.append(float(current_num) if '.' in current_num else int(current_num))
                    current_num = ""
                operators_list.append(char)
        
        if current_num:
            numbers.append(float(current_num) if '.' in current_num else int(current_num))
        
        i = 0
        while i < len(operators_list):
            if operators_list[i] in ('*', '/'):
                if operators_list[i] == '*':
                    result = numbers[i] * numbers[i + 1]
                else:
                    if numbers[i + 1] == 0:
                        print("Ошибка: деление на ноль!")
                        break
                    result = numbers[i] / numbers[i + 1]
                
                numbers[i] = result
                del numbers[i + 1]
                del operators_list[i]
            else:
                i += 1
        
        result = numbers[0]
        for i, op in enumerate(operators_list):
            if op == '+':
                result += numbers[i + 1]
            elif op == '-':
                result -= numbers[i + 1]
        
        print(f"Ответ: {result}")

try:
    while True:
        request = input(">>> ")
        socket = variating(request)
        print(socket)
except KeyboardInterrupt:
    print()
    stop = ""
    farewell(stop)
