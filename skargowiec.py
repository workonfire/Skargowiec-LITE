"""
Skargowiec Lite
by Buty935

Licensed under GPL 3.0
"""

from colors import color_print


def main():
    from engine import Engine
    import json
    import os
    import platform

    __EDITION__ = 'LITE'
    __VERSION__ = '1.0 BETA'
    __AUTHOR__ = ['Buty935', 'workonfire']

    if platform.system() == 'Windows':
        os.system('title Skargowiec LITE')
    color_print('red', "   _____ __                                  _              ")
    color_print('yellow', "  / ___// /______ __________ _____ _      __(_)__  _____")
    color_print('green', "  \\__ \\/ //_/ __ `/ ___/ __ `/ __ \\ | /| / / / _ \\/ ___/")
    color_print('blue', " ___/ / ,< / /_/ / /  / /_/ / /_/ / |/ |/ / /  __/ /__      ")
    color_print('cyan', "/____/_/|_|\\__,_/_/   \\__, /\\____/|__/|__/_/\\___/\\___/")
    color_print('magenta', "                     /____/                                 ")
    print("dla serwera GC2, by", __AUTHOR__[0])
    print("Wersja", __VERSION__)
    color_print('cyan', "Edycja " + __EDITION__)
    color_print('red', "\nUWAGA! Projekt Skargowca został porzucony.")
    color_print('red', "Wszelkie błędy oraz zapytania proszę kierować na Discorda: workonfire#8262\n")
    print("By rozpocząć działanie programu, wpisz 'start'. Lista komend: 'pomoc'.")

    if not os.path.isfile('data.json'):
        open('data.json', 'w').close()

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
            print("Lista komend:")
            commands = {'start': "uruchamia działanie Skargowca",
                        'podziekowania': "pokazuje listę szczególnych osób",
                        'reset': "resetuje plik konfiguracyjny",
                        'wzium': "wziumuje",
                        'pomoc': "pokazuje tę stronę"}
            for command in commands:
                print(f"{command} - {commands[command]}")
        elif command_line_input == 'wzium':
            color_print('red', "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            color_print('yellow', "██ ███ █▄▄ ██▄██ ██ █ ▄▀▄ ██")
            color_print('green', "██ █ █ █▀▄███ ▄█ ██ █ █▄█ ██")
            color_print('blue', "██▄▀▄▀▄█▄▄▄█▄▄▄██▄▄▄█▄███▄██")
            color_print('magenta', "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        elif command_line_input == '':
            pass
        else:
            color_print('red', "Nieznana komenda. By ujrzeć listę dostępnych komend, użyj polecenia \"pomoc\".")

    try:
        with open('data.json') as data_file:
            config = json.loads(data_file.read())
        color_print('green', f"Wczytano dane z poprzedniej konfiguracji ({config['nickname']}).")
    except json.decoder.JSONDecodeError:
        print("Uruchamiasz program po raz pierwszy. Wymagana jest wstępna konfiguracja.")
        color_print('red', "UWAGA! Wpisywane dane nie będą sprawdzane pod kątem poprawności.")
        color_print('red', "Jeśli program scrashuje, upewnij się, że wszystkie dane są poprawne.")
        forum_login = input("Login do Forum GC2: ")
        forum_password = input("Hasło do Forum GC2: ")
        nickname = input("Twój nick z gry: ")
        logs_path = input("Ścieżka do pliku z logami (Enter, jeśli chcesz pozostawić domyślną): ")
        wordlist_path = input("Ścieżka do pliku z listą słów (Enter, jeśli chcesz pozostawić domyślną): ")
        game_mode = input("Tryb, na którym będzie działać Skargowiec (np. SkyBlock 1): ").lower()
        if platform.system() == 'Windows':
            logs_path = os.getenv('APPDATA') + '\\.minecraft\\logs\\latest.log' if logs_path == '' else logs_path
            wordlist_path = os.path.dirname(
                os.path.realpath(__file__)) + '\\slowa.txt' if wordlist_path == '' else wordlist_path
        elif platform.system() == 'Linux':
            logs_path = os.getenv('HOME') + '/.minecraft/logs/latest.log' if logs_path == '' else logs_path
            wordlist_path = os.path.dirname(
                os.path.realpath(__file__)) + '/slowa.txt' if wordlist_path == '' else wordlist_path
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
        print()
        color_print('green', "Pomyślnie zapisano dane.")
        color_print('yellow',
                    "INFO: Możesz zdefiniować własne słowa, które program będzie wykrywał na czacie, w pliku slowa.txt "
                    "znajdującym się w katalogu instalacyjnym programu.")
    color_print('green', f"\nUruchomiono skanowanie czatu na trybie {config['game_mode']}.")
    print(
        "Możesz teraz zminimalizować program. Ujrzysz powiadomienie, kiedy Skargowiec będzie wymagał potwierdzenia "
        "przed wysłaniem skargi.")

    Engine().start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        color_print('red', "Działanie programu zostało zakończone.")
