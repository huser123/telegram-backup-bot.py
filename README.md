# Telegram Backup Bot

## Leírás
Ez a Python-alapú Telegram bot Linux rendszereken készített mentéseket tölt fel egy megadott Telegram beszélgetésbe. A bot automatikusan létrehozza a mentést, darabolja a fájlokat, és feltölti azokat.

---

## Fő funkciók
1. **Mentések létrehozása:**
   - A `/bot/mentes/` könyvtár tartalmából ZIP mentést készít.
   - A ZIP fájlok 49 MB-os darabokra vannak osztva a Telegram fájlméret-korlát miatt.

2. **Automatikus feltöltés:**
   - Az előkészített fájlokat feltölti a megadott Telegram beszélgetésbe.

3. **Mentés törlése:**
   - A mentés feltöltése után a bot törli az ideiglenes fájlokat a `/bot/tmp/` könyvtárból.

---

## Használat

### 1. **Beállítások**
- A kódban cseréld ki az alábbi változókat a saját értékeidre:
  - `TOKEN`: A Telegram botod tokenje.
  - `CHAT_ID`: Annak a beszélgetésnek az azonosítója, ahová a fájlokat fel akarod tölteni.

### 2. **Könyvtárak előkészítése**
- Hozd létre a következő könyvtárakat, ha még nem léteznek:
  - `/bot/mentes/`: A mentés forráskönyvtára.
  - `/bot/tmp/`: Az ideiglenes fájlok könyvtára.

### 3. **Futtatás**
- A bot futtatásához használd a következő parancsot:
  ```bash
  python3 telegram-backup-bot.py
  ```

---

## Követelmények
- Python 3
- `telebot` könyvtár telepítése:
  ```bash
  pip install pyTelegramBotAPI
  ```
- Linux operációs rendszer
- ZIP és alapvető Linux parancsok támogatása (pl. `zip`)

---


