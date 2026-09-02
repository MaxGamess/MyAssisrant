from time import *
from random import *
from sys import *
from datetime import datetime, date, time, timedelta
import pyttsx3
import threading
import webbrowser
import subprocess
import os
from translate import Translator

request = ""
socket = ""

def variating(socket):
    request_fix = request.lower()
    ultimate_words = {"привет", "хай", "здарова", "ку", "йоу", "старт", "салам", "qq", "вернулся", "пока", "алибидерчи", "бб", "стоп", "калькулятор", "счет", "считать", "год", "дата", "время", "време", "день", "суток", "открой", "сайт", "запусти", "переведи", "перевод"}
    varity = {
        'greeting': {"привет", "хай", "здарова", "ку", "старт", "салам", "qq", "йоу"},
        'farewell': {"пока", "алибидерчи", "бб", "стоп"},
        'comeback': {"вернулся"},
        'calc': {"калькулятор", "счет", "считать"},
        'date': {"дата", "день", "время", "време", "год", "суток"},
        'open': {"открой", "запусти"},
        'translate': {"переведи", "перевод"}
    }
    words = set(request_fix.split())
    
    if varity['greeting'] & words and "калькулятор" not in request_fix:
        return greeting(request_fix)
    if varity['comeback'] & words:
        return comeback(request_fix)
    if varity['farewell'] & words:
        return farewell(request_fix)
    if varity['calc'] & words:
        rqst = ""
        result = calculator(rqst)
        if result == "вернулся":
            return comeback(result)
    if varity['date'] & words:
        return date(request_fix)
    if varity['open'] & words:
        if "сайт" in request_fix:
            return open_link(request_fix)
        else:
            return open_prog(request_fix)
    if varity['translate'] & words:
        lang = "ru"
        if "русский" in request_fix:
            index = request_fix.find("русский")
            result = request_fix[index + len("русский"):]
            lang = "ru"
            return translator(result, lang)
        elif "английский" in request_fix:
            index = request_fix.find("английский")
            result = request_fix[index + len("английский"):]
            lang = "en"
            return translator(result, lang)
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

def translator(socket, lang):
    sct = "Перевод"
    translators = {
        "ru": Translator(to_lang="ru"),
        "en": Translator(to_lang="en")
    }
    
    translator = translators[lang]
    result = translator.translate(socket)
    
    if socket.count(" ") > 1:
        return f"{sct} данного предложения: {result}"
    else:
        return f"{sct} данного слова: {result}"

def open_link(socket):
    links = {
        "ютуб": "https://youtube.com",
        "тг": "https://t.me/",
        "дс": "https://discord.com/",
        "вк": "https://vk.com/",
        "гугл": "https://google.com/",
        "яндекс": "https://ysndex.ru/",
        "гитхаб": "https://github.com/",
        "модринт": "https://modrinth.com/",
        "маин": "https://minecraft.net/",
    }
    
    for key in links:
        if key in socket:
            webbrowser.open_new(links[key])
            return f"Открываю сайт {key}"

def open_prog(socket):
    appdata = os.environ.get('APPDATA')
    localappdata = os.environ.get('LOCALAPPDATA')
    
    #для подписчиков гитхаб и тг - добавьте сами пути на свои программы
    progs = {
        "пример": "C:/Program Files/пример.exe",
    }
    
    for key in progs:
        if key in socket:
            os.startfile(progs[key])
            return f"Открываю {key}"

def farewell(socket):
    def_sct = "До свиданнья"
    sct = ""
    rnd = randint(0,2)
    if rnd == 0:
        sct = def_sct + ", сэр!"
        print(sct)
        say_async(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
        exit()
    elif rnd == 1:
        sct = "До следующего сеанса!"
        print(sct)
        say_async(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
        exit()
    else:
        sct = def_sct + "!"
        print(sct)
        say_async(sct)
        sleep(3)
        print("Завершение работы...")
        sleep(1)
    
    return exit()

def date(socket):
    rnd = randint(0,2)
    today = ""
    sct = ""
    now_time = ""
    now_date = ""
    current_time = localtime()
    current_weekday = 0
    
    days = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"
    }
    
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    if rnd == 0:
        sct = "На данный момент: "
    elif rnd == 1:
        sct = "Прямо сейчас: "
    else:
        sct = "Щас: "
    
    if "дата" in socket:
        today = str(datetime.now())
        now_date = sct + today[:10]
        return now_date
    
    elif ("время" in socket or "време" in socket) and "суток" not in socket:
        now_time = f"{sct}{hours} часов, {minutes} минут, {seconds} секунд"
        return now_time
    
    elif "день" in socket:
        today = str(datetime.now())
        now_day_year = int(today[:4])
        now_day_month = int(today[5:7])
        now_day_day = int(today[9:10])
        current_weekday = datetime(now_day_year, now_day_month, now_day_day)
        now_day = current_weekday.weekday()
        
        now_weekday = sct + days[now_day]
        return now_weekday
    
    elif "год" in socket:
        today = str(datetime.now())
        now_day_year = today[:4]
        return f"{sct}{now_day_year} год"
    
    elif "суток" in socket:
        if hours >= 0 and hours < 4: day_time = "ночь"
        elif hours >= 4 and hours < 12: day_time = "утро"
        elif hours >= 12 and hours < 16: day_time = "день"
        elif hours >= 16 and hours < 24: day_time = "вечер"
        
        return sct + day_time
        

def calculator(socket):
    operators = {"+", "-", "*", "/", "^"}
    rqst = ""
    
    while True:
        rqst = input("calc mod >>> ")
        
        fix_rqst = rqst.lower()
        cleaned = fix_rqst.replace(" ", "")
        word = set("0123456789+-*/^().")
        char = ""
        valid = True
        for char in cleaned:
            if char not in word:
                return "вернулся"
                valid = False
                break
        if not valid:
            continue
        
        try:
            while '(' in cleaned:
                
                start = -1
                end = -1
                
                for i in range(len(cleaned)):
                    if cleaned[i] == '(':
                        start = i
                    elif cleaned[i] == ')' and start != -1:
                        end = i
                        break
                
                if start == -1 or end == -1:
                    print("Обнаружено несоответствие скобок!")
                    break
                
                inner_expr = cleaned[start + 1:end]
                
                numbers, operators_list, current_num = [], [], ""
                
                for char in inner_expr:
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
                    if operators_list[i] == '^':
                        result = numbers[i] ** numbers[i + 1]
                        numbers[i] = result
                        del numbers[i + 1]
                        del operators_list[i]
                    else:
                        i += 1
                
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
                
                cleaned = cleaned[:start] + str(result) + cleaned[end + 1:]
            
            numbers, operators_list, current_num = [], [], ""
            
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
                if operators_list[i] == '^':
                    result = numbers[i] ** numbers[i + 1]
                    numbers[i] = result
                    del numbers[i + 1]
                    del operators_list[i]
                else:
                    i += 1
            
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
        
        except Exception as e:
            print(f"Ошибка: {e}")

def say_async(socket):
    def _say():
        try:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voice[0].id)
            engine.setProperty('volume', 0.5)
            engine.say(socket)
            engine.runAndWait()
            engine.stop()
        except:
            pass
    threading.Thread(target=_say, daemon=True).start()

try:
    while True:
        request = input(">>> ")
        socket = variating(request)
        print(socket)
        say_async(socket)
    
except KeyboardInterrupt:
    print()
    stop = ""
    farewell(stop)
