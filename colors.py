import colorama
def color_print(color, text):
    colorama.init(autoreset = True)
    colors = {'red': colorama.Fore.RED,
              'green': colorama.Fore.GREEN,
              'yellow': colorama.Fore.YELLOW,
              'blue': colorama.Fore.BLUE,
              'magenta': colorama.Fore.MAGENTA,
              'cyan': colorama.Fore.CYAN,
              'white': colorama.Fore.WHITE}
    print(colorama.Style.BRIGHT + colors.get(color) + text)
    colorama.deinit()