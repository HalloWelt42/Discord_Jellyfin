# Jellyfin Discord Rich Presence 🎵

<!-- Platz für deine Werbegrafik -->
![Jellyfin Discord Rich Presence Banner](./media/Bildschirmfoto%202025-07-20%20um%2016.41.21.png)

> Zeige deinen Freunden auf Discord, welche Musik du gerade über Jellyfin hörst!

## 📋 Übersicht

Dieses Python-Script verbindet deinen Jellyfin Media Server mit Discord Rich Presence. Sobald du Musik über Jellyfin abspielst, wird automatisch der aktuelle Song in deinem Discord-Status angezeigt.

### ✨ Features

- 🎵 **Automatische Musikerkennung** - Zeigt Titel, Künstler und Album
- ⏱️ **Live-Updates** - Status wird alle 5 Sekunden aktualisiert
- 💤 **Idle-Modus** - Zeigt benutzerdefinierten Text wenn keine Musik läuft
- 🖥️ **Plattformübergreifend** - Funktioniert auf Windows, macOS und Linux
- 🔒 **Privat & Sicher** - Läuft lokal, keine Cloud-Dienste

## 🚀 Schnellstart

### Voraussetzungen

- Python 3.7+
- Jellyfin Server (lokal oder remote)
- Discord Desktop App
- 10 Minuten Zeit für die Einrichtung

### Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/yourusername/jellyfin-discord-rpc.git
   cd jellyfin-discord-rpc
   ```

2. **Virtuelle Umgebung erstellen** (empfohlen)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # oder
   .venv\Scripts\activate     # Windows
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfiguration einrichten**
   ```bash
   cp .env.example .env
   ```
   Bearbeite die `.env` Datei mit deinen Zugangsdaten (siehe [Konfiguration](#konfiguration))

5. **Script starten**
   ```bash
   python main.py
   ```

## ⚙️ Konfiguration

Die Konfiguration erfolgt über die `.env` Datei:

```env
# Jellyfin Server
JELLYFIN_URL=http://localhost:8096    # Deine Jellyfin Server URL
API_KEY=dein_jellyfin_api_key         # Siehe: docs/jellyfin-setup.md
USER_ID=deine_jellyfin_user_id        # Deine Jellyfin User ID

# Discord
DISCORD_CLIENT_ID=123456789012345678   # Siehe: docs/discord-setup.md

# Optional
IDLE_TEXT=🎵 Musik mit Jellyfin       # Text wenn keine Musik läuft
```

### 📚 Anleitungen

- **[Jellyfin API Key einrichten](docs/jellyfin-setup.md)** - Schritt-für-Schritt Anleitung
- **[Discord Application erstellen](docs/discord-setup.md)** - Mit Screenshots
- **[Allgemeine Hinweise & FAQ](docs/general-info.md)** - Troubleshooting & Tipps

## 📁 Projektstruktur

```
jellyfin-discord-rpc/
│
├── 📄 main.py              # Hauptprogramm
├── 📄 requirements.txt     # Python-Abhängigkeiten
├── 📄 .env.example         # Beispiel-Konfiguration
├── 📄 .env                 # Deine Konfiguration (nicht in Git!)
├── 📄 .gitignore          # Git-Ausschlüsse
├── 📄 README.md           # Diese Datei
│
├── 📁 docs/               # Dokumentation
│   ├── 📄 jellyfin-setup.md
│   ├── 📄 discord-setup.md
│   └── 📄 general-info.md
│
└── 📁 .venv/              # Python Virtual Environment
```

## 🎯 Verwendung

Nach dem Start läuft das Script kontinuierlich und:

1. Verbindet sich mit Discord Rich Presence
2. Prüft alle 5 Sekunden den Jellyfin-Status
3. Aktualisiert deinen Discord-Status automatisch
4. Zeigt einen Idle-Text wenn keine Musik läuft

**Beenden**: Drücke `Ctrl+C` im Terminal

### Discord-Anzeige

So sieht es in Discord aus:

```
🎵 Bohemian Rhapsody
Queen – A Night at the Opera
━━━━━━━━━━━━━━━━━━━
Spielt seit 2:34
```

## 🔧 Troubleshooting

### Häufige Probleme

1. **"Discord nicht gefunden"**
   - Stelle sicher, dass Discord läuft
   - Aktiviere "Zeige aktuelle Aktivität" in Discord-Einstellungen

2. **"Keine Musik erkannt"**
   - Prüfe ob Jellyfin läuft
   - Verifiziere deine API-Credentials
   - Stelle sicher, dass du Musik (nicht Videos) abspielst

3. **macOS-spezifisch**
   ```bash
   # Discord neu starten
   killall Discord && open -a Discord
   ```

Weitere Hilfe findest du in den [Allgemeinen Hinweisen](docs/general-info.md).

## 🤝 Beitragen

Contributions sind willkommen! Bitte erstelle einen Pull Request oder öffne ein Issue.

## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

## 🙏 Credits

- Jellyfin Team für den großartigen Media Server
- Discord für Rich Presence API
- pypresence Bibliothek

---

**Entwickelt mit ❤️ für die Jellyfin Community**