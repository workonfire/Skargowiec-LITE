"""
Skargowiec Lite
by Buty935
"""

from engine import Engine
from colors import color_print
import json
import os
__EDITION__ = 'LITE'
__VERSION__ = '1.0 BETA'
__AUTHOR__ = 'Buty935'

os.system('title Skargowiec LITE')
color_print('red', "   _____ __                                  _              ")
color_print('yellow', "  / ___// /______ __________ _____ _      __(_)__  _____")
color_print('green', "  \__ \/ //_/ __ `/ ___/ __ `/ __ \ | /| / / / _ \/ ___/")
color_print('blue', " ___/ / ,< / /_/ / /  / /_/ / /_/ / |/ |/ / /  __/ /__      ")
color_print('cyan', "/____/_/|_|\__,_/_/   \__, /\____/|__/|__/_/\___/\___/")
color_print('magenta', "                     /____/                                 ")
print("dla serwera GC2, by", __AUTHOR__)
print("Wersja", __VERSION__)
color_print('cyan', "Edycja " + __EDITION__)
color_print('red', "UWAGA! Ta wersja Skargowca nie jest wersją finalną. Program w wersji okienkowej z graficznym, ")
color_print('red', "przyjaznym dla użytkownika interfejsem jest już prawie skończony, jednak ze względu na")
color_print('red', "nacisk użytkowników wydałem pośpiesznie wersję konsolową, która w 100% spełnia swoje zadanie.")
color_print('red', "Wszelkie błędy oraz sugestie proszę zgłaszać na Discordzie: workonfire#8262")
print()

print("By rozpocząć działanie programu, wpisz 'start'. Lista komend: 'pomoc'.")
while True:
    command_line_input = input("Skargowiec> ").lower()
    if command_line_input == 'start':
        break
    elif command_line_input == 'podziekowania':
        print("Chciałbym serdecznie podziękować dwóm osobom za pomoc przy tworzeniu programu:")
        color_print('cyan', "Yukas, za wsparcie psychiczne <3")
        color_print('cyan', "jjay31, za ciągłe mówienie mi, bym porzucił ten projekt <3")
    elif command_line_input == 'reset':
        with open('data.json', 'r+') as configuration_file:
            configuration_file.truncate()
        color_print('green', "Konfiguracja została zresetowana.")
    elif command_line_input == 'pomoc':
        commands = {'start': "uruchamia działanie Skargowca",
                    'podziekowania': "pokazuje listę szczególnych osób",
                    'reset': "resetuje plik konfiguracyjny",
                    'pomoc': "pokazuje tę stronę"}
        print("Lista komend:")
        for key in commands:
            print(key + ' - ' + commands[key])
    else:
        color_print('red', "Nieznana komenda")

try:
    with open('data.json') as data_file:
        config = json.loads(data_file.read())
    color_print('green', "Wczytano dane z poprzedniej konfiguracji ({}).".format(config['nickname']))
except json.decoder.JSONDecodeError:
    print("Uruchamiasz program po raz pierwszy. Wymagana jest wstępna konfiguracja.")
    color_print('red', "UWAGA! Wpisywane dane nie będą sprawdzane pod kątem poprawności.")
    forum_login = input("Login do Forum GC2: ")
    forum_password = input("Hasło do Forum GC2: ")
    nickname = input("Twój nick z gry: ")
    logs_path = input("Ścieżka do pliku z logami (wpisz D, jeśli chcesz pozostawić domyślną): ")
    wordlist_path = input("Ścieżka do pliku z listą słów (wpisz D, jeśli chcesz pozostawić domyślną): ")
    game_mode = input("Tryb, na którym będzie działać Skargowiec (np. skyblock 1): ").lower()
    if logs_path.upper() == 'D':
        logs_path = os.getenv('APPDATA') + '\\.minecraft\\logs\\latest.log'
    if wordlist_path.upper() == 'D':
        wordlist_path = os.path.dirname(os.path.realpath(__file__)) + '\\slowa.txt'
    with open('data.json', 'w') as data_file:
        data = {
            "forum_login": forum_login,
            "forum_password": forum_password,
            "nickname": nickname,
            "logs_path": logs_path,
            "wordlist_path": wordlist_path,
            "game_mode": game_mode
            }
        json.dump(data, data_file)
    with open('data.json') as data_file:
        config = json.loads(data_file.read())
    color_print('green', "Pomyślnie zapisano dane.")
    print("Możesz zdefiniować własne słowa, które program będzie wykrywał na czacie, w pliku slowa.txt znajdującym się w katalogu instalacyjnym programu.")
color_print('green', "Uruchomiono skanowanie czatu na trybie {}.".format(config['game_mode']))
print("Możesz teraz zminimalizować program. Ujrzysz powiadomienie, kiedy Skargowiec będzie wymagał potwierdzenia przed wysłaniem skargi.")

engine = Engine()
engine.engine_start()
