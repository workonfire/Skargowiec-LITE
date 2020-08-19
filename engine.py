import chatscanner
import json
import pyautogui
import threading
import win10toast
import win32gui
from base64 import b64encode
from time import sleep
from time import strftime
from requests import post
from forumapi import GC2
from colors import color_print


def screenshot(window_title=None):
    # FIXME: Multi-monitor support
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            raise OSError("Window not found.")
    else:
        im = pyautogui.screenshot()
        return im


class Engine:
    def __init__(self):
        self.window_alert = True
        with open('data.json') as data_file:
            self.config = json.loads(data_file.read())
        self.chat = chatscanner.Scanner(self.config['logs_path'], 'slowa.txt')

        def __chat_worker():
            self.chat.scan()

        self.scanner_thread = threading.Thread(target=__chat_worker)
        self.scanner_thread.setDaemon(True)
        self.scanner_thread.start()
        self.__IMGUR_CLIENT_ID__ = ''
        self.__IMGUR_API_KEY__ = ''

    def start(self):
        """
        Starts the main engine.
        :return:
        """
        while True:
            if self.chat.warning:
                while "Minecraft" not in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
                    if self.window_alert:
                        toast = win10toast.ToastNotifier()
                        toast.show_toast("Zmień okno na Minecraft!", "Skargowiec musi zrobić screena.",
                                         icon_path='icon.ico')
                        self.window_alert = False
                    sleep(0.5)
                self.window_alert = True
                self.chat.warning = False

                with open('temp/last.json', 'w') as last_complaint_file:
                    data = {
                        'nickname': self.config['nickname'],
                        'charged_user_nick': self.chat.charged_user_nick,
                        'date': strftime("%d.%m.%Y"),
                        'gamemode': self.config['game_mode'],
                        'screenshot': 'temp/screenshot.png',
                        'description': "Słowa"
                    }
                    json.dump(data, last_complaint_file)

                screenshot(win32gui.GetWindowText(win32gui.GetForegroundWindow())).save('temp/screenshot.png')
                toast = win10toast.ToastNotifier()
                toast.show_toast("Wróć do Skargowca!", "Skargowiec wymaga od ciebie potwierdzenia wysłania skargi.",
                                 icon_path='icon.ico')
                color_print('red', '----------------')
                color_print('red', "Wysyłanie skargi")
                color_print('red', '----------------')

                print("Jeśli chcesz anulować wysyłanie skargi, zamknij program.")
                print("Czy poniższe dane się zgadzają? Jeśli tak, naciśnij Enter.")
                nickname = input(f"Twój nick ({self.config['nickname']}) >> ")
                charged_user = input(f"Nick oskarżonego ({self.chat.charged_user_nick}) >> ")
                date = input(f"Data ({strftime('%d.%m.%Y')}) >> ")
                gamemode = input(f"Tryb ({self.config['game_mode']}) >> ")
                screenshot_filename = input("Zrzut ekranu (temp/screenshot.png) >> ")
                description = input("Opis (słowa) >> ")
                nickname = self.config['nickname'] if nickname == '' else self.config['nickname']
                screenshot_filename = "temp/screenshot.png" if screenshot_filename == '' else screenshot_filename
                charged_user = self.chat.charged_user_nick if charged_user == '' else charged_user
                date = strftime("%d.%m.%Y") if date == '' else date
                gamemode = self.config['game_mode'] if gamemode == '' else gamemode
                description = "Słowa" if description == '' else description
                game_modes = {'skyblock 1': 14,
                              'skyblock 2': 14,
                              'skyblock 3': 14,
                              'skyblock 4': 14,
                              'skyblock 5': 14,
                              'mineblock 1': 25,
                              'mineblock 2': 25,
                              'creative': 29,
                              'classicmc': 33,
                              'seablock': 37,
                              'lavablock': 294}

                print("Trwa przesyłanie zrzutu ekranu...")
                screenshot_request = post(url="https://api.imgur.com/3/upload.json",
                                          headers={
                                              'Authorization': f"Client-ID {self.__IMGUR_CLIENT_ID__}"},
                                          data={'key': self.__IMGUR_API_KEY__,
                                                'image': b64encode(open(screenshot_filename, 'rb').read()),
                                                'type': 'base64',
                                                'name': 'screenshot.png',
                                                'title': 'Zrzut ekranu - Skargowiec'})
                imgur_link = json.loads(screenshot_request.text)['data']['link']

                print("Trwa wrzucanie skargi na Forum...")
                forum_session = GC2()
                forum_session.login(username=self.config['forum_login'],
                                    password=self.config['forum_password'])
                forum_session.create_thread(forum_category=game_modes.get(gamemode),
                                            prefix=25,
                                            icon=2,
                                            subject=f"Skarga na {charged_user}",
                                            message=f"Mój nick: {nickname}\n" +
                                                    f"Nick oskarżonego: {charged_user}\n" +
                                                    f"Data: {date}\n" +
                                                    f"Serwer: {gamemode.lower()}\n" +
                                                    f"Opis: {description}\n" +
                                                    f"Dowód: {imgur_link}")

                color_print('green', "Skarga wrzucona! Możesz znów zminimalizować program.")
            sleep(0.5)
