# Skargowiec | wersja LITE
Program do automatycznego pisania skarg przystosowany do serwera GC2.

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
Pliki binarne (`.exe`) ani instalatory nie zostaną udostępnione z przyczyn prywatnych oraz dlatego, że nie lubię `pyinstaller`a.

## Instalacja
Jeśli mimo wszystko chcesz uruchomić ten program, postępuj zgodnie z poniższymi instrukcjami.

Do instalacji wymagany jest [Python 3](https://www.python.org/downloads/).

- By zainstalować wszystkie potrzebne biblioteki i zależności, użyj komendy `python -m pip install -r requirements.txt`.
- Uzupełnij dane do API Imgura znajdujące się w pliku `engine.py` w linijkach
```python
self.__IMGUR_CLIENT_ID__ = ''
self.__IMGUR_API_KEY__ = ''
```
- Następnie uruchom program poleceniem `python skargowiec.py`.

**UWAGA:** Przed użyciem programu SKONFIGURUJ słowa w pliku `slowa.txt`

**UWAGA 2:** Nie odpowiadam za wykorzystywanie programu do nieodpowiednich celów. Uruchamiając go bierzesz na własną odpowiedzialność to, w jaki sposób będziesz się z nim obchodził.

## Kontakt
Wszelkie pytania, sugestie, proszę kierować na Discorda: *workonfire#8262*, lub na GitHub Issue Trackera.

## Informacja
Pełna wersja graficznego Skargowca nie zostanie nigdy udostępniona, bo nie miałem okazji jej dokończyć, a projekt jest już niewspierany.
Jeśli jednak ktoś chciałby wiedzieć, jak miała wyglądać, poniżej znajdują się screeny.

![Screenshot 2](https://cdn.discordapp.com/attachments/678319256546312272/695804289653669969/unknown.png)
![Screenshot 3](https://cdn.discordapp.com/attachments/678319256546312272/695804318858608660/unknown.png)
![Screenshot 4](https://cdn.discordapp.com/attachments/678319256546312272/695804345144574022/unknown.png)
![Screenshot 5](https://cdn.discordapp.com/attachments/678319256546312272/695804371660963920/unknown.png)
![Screenshot 6](https://cdn.discordapp.com/attachments/678319256546312272/695804791409868830/unknown.png)
![Screenshot 7](https://cdn.discordapp.com/attachments/678319256546312272/695816401407049728/unknown.png)
![Screenshot 8](https://cdn.discordapp.com/attachments/678319256546312272/695816707343646780/skargowiec.png)
Nie, nie było wersji na Maka. Ostatni screen to zabawa z Adobe XD.
