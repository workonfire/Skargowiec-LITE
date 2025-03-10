# Skargowiec | wersja LITE
Program do automatycznego pisania skarg przystosowany do serwera GC2. **Już nie działa**.

![Screenshot](https://i.imgur.com/rkWfCU1.png)

## Funkcje
- Skanowanie czatu w tle pod względem wulgaryzmów, floodu itp.
- Możliwość skonfigurowania listy słów, które Skargowiec ma wykrywać
- Automatyczne zapisywanie dowodu w postaci screenshota okna Minecraft
- Automatyczne wrzucanie screenshota na Imgura i postowanie skargi na forum w odpowiednim dziale
- Inteligentne powiadomienia o konieczności zatwierdzenia skargi i zrobienia screena
- Zapamiętywanie sesji logowania do forum
- Możliwość podmiany treści skargi (w tym dowodu) w razie, gdyby coś się nie udało lub powód zgłaszania był inny

## Pobieranie
Do pobrania dostępny jest jedynie kod źródłowy.

## Instalacja
Jeśli mimo wszystko chcesz uruchomić ten program, postępuj zgodnie z poniższymi instrukcjami.

Do instalacji wymagany jest [Python 3](https://www.python.org/downloads/).

- By zainstalować wszystkie potrzebne biblioteki i zależności, użyj polecenia `python -m pip install -r requirements.txt`.
- Uzupełnij dane do [API Imgura](https://apidocs.imgur.com/?version=latest) znajdujące się w pliku `engine.py` w linijkach
```python
self.__IMGUR_CLIENT_ID__ = ''
self.__IMGUR_API_KEY__ = ''
```
- *(Opcjonalnie)* Przed użyciem programu skonfiguruj słowa w pliku `slowa.txt`
- Uruchom program poleceniem `python skargowiec.py`.

**UWAGA:** Nie odpowiadam za wykorzystywanie programu do nieodpowiednich celów. Uruchamiając go bierzesz [na własną odpowiedzialność](https://github.com/workonfire/Skargowiec-LITE/blob/master/LICENSE#L589) to, w jaki sposób będziesz się z nim obchodził.

## Dystrybucja
- Zainstaluj moduł `pyinstaller` poleceniem `python -m pip install pyinstaller`.
- Użyj polecenia `pyinstaller -i icon.ico skargowiec.py`.
- Wytworzony plik *.exe* będzie znajdował się w katalogu `dist`.

## Kontakt
Wszelkie pytania, sugestie, proszę kierować na Discorda: **workonfire#8262** lub na [GitHub Issue Trackera](https://github.com/workonfire/Skargowiec-LITE/issues).

## Informacja
Pełna wersja graficznego Skargowca nie zostanie nigdy udostępniona, bo nie miałem okazji jej dokończyć, a projekt jest już niewspierany.
Jeśli jednak ktoś chciałby wiedzieć, jak miała wyglądać, poniżej znajdują się screeny.

![Screenshot 2](https://i.imgur.com/Ag19OPu.png)
![Screenshot 3](https://i.imgur.com/evkjmMw.png)
![Screenshot 4](https://i.imgur.com/nttquxQ.png)
![Screenshot 5](https://i.imgur.com/v9Wrxyg.png)
