# D&D Light - Wersja 0.3

**Autor:** Illia Skakun

## 1. Opis działania projektu
„D&D Light” to tekstowa gra RPG inspirowana klasycznym systemem Dungeons & Dragons. Gracz wciela się w poszukiwacza przygód, eksploruje lokacje i podejmuje decyzje, które mają bezpośredni wpływ na przebieg rozgrywki (np. wybór ścieżki w jaskini czy sposób podejścia do przeciwnika).

### Główne mechaniki:
* **Tworzenie bohatera:** Gracz na początku gry podaje swoje imię i wybiera jedną z 5 dostępnych klas (Archer, Wizard, Gnome, Ogr, Knight). Każda z nich posiada unikalną wartość punktów zdrowia oraz specyficzną broń.
* **System questów i decyzji:** Przechodzenie przez kolejne etapy gry opiera się na wyborach tekstowych. Sukces niektórych akcji (np. przekradanie się) zależy od wbudowanego systemu szans/szczęścia wyliczanego na podstawie losowości.
* **System walki:** Walka odbywa się w systemie turowym z losowo generowanymi przeciwnikami (np. Zombie, Skeleton, Giant). Ataki gracza opierają się na statystykach posiadanej broni, podczas gdy obrażenia otrzymywane od wrogów są częściowo losowe. Gdy punkty życia spadną poniżej zera, gra wyrzuca specjalny wyjątek `DeathException` i kończy rozgrywkę.
* **Logowanie:** Gra posiada wbudowany system logowania (plik `Logger.py`), który automatycznie zapisuje przebieg gry i informacje debugowania w folderze `logs/`.

## 2. Instrukcja uruchomienia

### Wymagania:
* **Python w wersji 3.10 lub nowszej.** (Projekt korzysta ze struktury `match-case` w pliku `Entities.py`, która nie jest obsługiwana w starszych wersjach).
* Standardowe biblioteki Pythona (moduły takie jak `os`, `json`, `logging`, `random` są wbudowane, więc nie trzeba instalować niczego za pomocą `pip`).

### Jak uruchomić:
1. Pobierz lub sklonuj wszystkie pliki projektu (.py) do jednego wspólnego folderu.
2. Otwórz terminal (lub wiersz poleceń) i przejdź do folderu z grą.
3. Uruchom główny skrypt, wpisując poniższą komendę:
   python3 main.py