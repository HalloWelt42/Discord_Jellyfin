# Discord Application einrichten 🎮

Diese Anleitung zeigt dir, wie du eine Discord Application für Rich Presence erstellst.

## 📋 Voraussetzungen

- Discord Account
- Discord Desktop App (Rich Presence funktioniert NICHT im Browser!)
- 5 Minuten Zeit

## 🚀 Discord Application erstellen

### 1. Discord Developer Portal öffnen

Gehe zu: **[https://discord.com/developers/applications](https://discord.com/developers/applications)**

### 2. Neue Application erstellen

1. Klicke auf **"New Application"** (blauer Button oben rechts)
2. **Name eingeben**: z.B. `Jellyfin Music` oder `My Media Player`
   - Dieser Name wird in Discord angezeigt!
   - Wähle einen aussagekräftigen Namen
3. Akzeptiere die Developer Terms
4. Klicke auf **"Create"**

### 3. Application ID kopieren

1. Du landest auf der **"General Information"** Seite
2. Unter **Application ID** findest du eine lange Nummer
3. **Kopiere diese ID** - das ist deine `DISCORD_CLIENT_ID`

```env
DISCORD_CLIENT_ID=1234567890123456789
```

### 4. Rich Presence konfigurieren (Optional)

1. Im linken Menü: **"Rich Presence"** → **"Art Assets"**
2. Hier kannst du eigene Icons hochladen:
   - `music` - Großes Icon (min. 512x512px)
   - `play` - Kleines Status-Icon
   - `pause` - Pause-Icon

**Hinweis**: Das Script funktioniert auch ohne eigene Icons!

## ⚙️ Discord-Einstellungen prüfen

### Aktivitätsstatus aktivieren

**WICHTIG**: Ohne diese Einstellung wird nichts angezeigt!

1. **Discord öffnen** (Desktop App)
2. **Einstellungen öffnen**:
   - Windows/Linux: `Strg + ,`
   - macOS: `Cmd + ,`
   - Oder: Zahnrad neben deinem Namen

3. **Aktivitätsstatus**:
   - Links im Menü → **"Aktivitätsstatus"**
   - **"Zeige aktuelle Aktivität als Status-Nachricht"** → **AN** ✅

4. **Discord neu starten** (empfohlen)

## 🧪 Verbindung testen

### Quick-Test Script

Erstelle eine Datei `discord_test.py`:

```python
from pypresence import Presence
import time

CLIENT_ID = "DEINE_CLIENT_ID_HIER"  # Hier deine ID eintragen!

try:
    # Verbinden
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    print("✅ Verbunden!")
    
    # Status setzen
    rpc.update(
        details="Test erfolgreich!",
        state="Setup funktioniert",
        start=int(time.time())
    )
    print("📢 Schau jetzt in Discord!")
    
    # 30 Sekunden warten
    time.sleep(30)
    
    # Aufräumen
    rpc.close()
    
except Exception as e:
    print(f"❌ Fehler: {e}")
```

Führe aus mit: `python discord_test.py`

## 🎨 Rich Presence Anpassungen

### Icon-Namen im Script

Das Script verwendet diese Icon-Namen:
- `music` - Haupticon
- `play` - Spielt gerade
- `pause` - Pausiert

### Custom Icons hochladen

1. Developer Portal → Deine App → **Rich Presence** → **Art Assets**
2. **"Add Image(s)"** klicken
3. Bilder hochladen (PNG/JPG, min. 512x512px)
4. **Asset Name** vergeben (z.B. `music`)
5. **Save Changes**

**Tipp**: Icons sind nach 5-10 Minuten verfügbar!

## 🖥️ Plattform-spezifische Hinweise

### Windows
- Discord muss im Hintergrund laufen
- Windows Firewall kann die Verbindung blockieren

### macOS
- Bei Problemen: `killall Discord && open -a Discord`
- Prüfe Sicherheitseinstellungen in Systemeinstellungen

### Linux
- Stelle sicher dass Discord nicht als Flatpak läuft
- Native Installation empfohlen für Rich Presence

## ❓ Häufige Probleme

### "Could not connect to Discord"

1. **Discord läuft nicht**
   - Starte Discord Desktop App
   - Browser-Version unterstützt kein Rich Presence!

2. **Falscher Port**
   - Discord RPC nutzt Port 6463-6472
   - Firewall prüfen

3. **Alte Discord Version**
   - Update Discord auf die neueste Version

### "Rich Presence nicht sichtbar"

1. **Aktivitätsstatus prüfen**
   - Muss in Discord-Einstellungen aktiviert sein!

2. **Privatsphäre-Einstellungen**
   - Server-Einstellungen → Privatsphäre → Aktivitätsstatus

3. **Cache leeren** (macOS/Linux)
   ```bash
   rm -rf ~/.config/discord/Cache/*
   ```

### Client ID Probleme

- ID muss exakt 18-19 Ziffern lang sein
- Keine Leerzeichen oder andere Zeichen
- Groß-/Kleinschreibung egal (nur Zahlen)

## 🔗 Nützliche Links

- [Discord Developer Portal](https://discord.com/developers/applications)
- [Rich Presence Dokumentation](https://discord.com/developers/docs/rich-presence/how-to)
- [pypresence GitHub](https://github.com/qwertyquerty/pypresence)

## 💡 Tipps & Tricks

1. **App-Name wählen**
   - Wird als "Spielt **App-Name**" angezeigt
   - Kurz und prägnant halten

2. **Test-Server erstellen**
   - Erstelle einen privaten Discord-Server zum Testen
   - So störst du niemanden während der Einrichtung

3. **Entwickler-Modus**
   - Discord Einstellungen → Erweitert → Entwicklermodus
   - Erlaubt IDs zu kopieren mit Rechtsklick

---

[← Jellyfin Setup](jellyfin-setup.md) | [Allgemeine Hinweise →](general-info.md)