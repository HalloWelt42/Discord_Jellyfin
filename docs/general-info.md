# Allgemeine Hinweise & FAQ 📚

## 🎯 Was kann dieses Programm?

### Hauptfunktionen

- **Live-Musikstatus**: Zeigt in Discord, was du gerade in Jellyfin hörst
- **Automatische Updates**: Erkennt Songwechsel innerhalb von 3 Sekunden
- **Detaillierte Anzeige**: Titel, Künstler, Album und Spielzeit
- **Idle-Modus**: Zeigt benutzerdefinierten Text wenn keine Musik läuft
- **Ressourcenschonend**: Minimaler CPU/RAM-Verbrauch

### Was wird NICHT unterstützt

- ❌ Videos/Filme (nur Musik)
- ❌ Discord Browser-Version
- ❌ Mobile Discord Apps
- ❌ Mehrere Jellyfin-User gleichzeitig
- ❌ Spotify-Integration (nutze dafür Discord's native Integration)

## 💻 System-Voraussetzungen

### Software

| Komponente | Minimum | Empfohlen |
|------------|---------|-----------|
| Python | 3.7+ | 3.10+ |
| Jellyfin | 10.7+ | 10.8+ |
| Discord | Beliebig | Neueste Version |
| RAM | 50 MB | 100 MB |
| CPU | Minimal | Minimal |

### Unterstützte Betriebssysteme

- ✅ Windows 10/11
- ✅ macOS 10.15+ (Catalina oder neuer)
- ✅ Linux (Ubuntu, Debian, Arch, etc.)
- ⚠️ Raspberry Pi (funktioniert, aber Discord Desktop App benötigt)

## 🔧 Installation von Abhängigkeiten

### Discord installieren

**Windows/macOS**:
- Download von [discord.com](https://discord.com/download)
- Normale Installation durchführen

**Linux**:
```bash
# Ubuntu/Debian
sudo snap install discord

# Arch Linux
yay -S discord

# Flatpak (universal)
flatpak install flathub com.discordapp.Discord
```

### Jellyfin installieren

**Docker** (empfohlen):
```bash
docker run -d \
  --name jellyfin \
  -p 8096:8096 \
  -v /path/to/config:/config \
  -v /path/to/media:/media \
  jellyfin/jellyfin
```

**Native Installation**:
- [Jellyfin Downloads](https://jellyfin.org/downloads/)

### Python & pip

**Windows**:
- Download von [python.org](https://python.org)
- ✅ "Add Python to PATH" aktivieren!

**macOS**:
```bash
# Mit Homebrew
brew install python3
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip python3-venv

# Arch
sudo pacman -S python python-pip
```

## 🚀 Erweiterte Konfiguration

### Auto-Start einrichten

**Windows** (Task Scheduler):
1. `Win + R` → `taskschd.msc`
2. "Aufgabe erstellen"
3. Trigger: "Bei Anmeldung"
4. Aktion: `python C:\Pfad\zu\main.py`

**macOS** (launchd):
```bash
# Erstelle ~/Library/LaunchAgents/com.jellyfin.discord.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jellyfin.discord</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/Users/DeinName/jellyfin-discord/main.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>

# Aktivieren
launchctl load ~/Library/LaunchAgents/com.jellyfin.discord.plist
```

**Linux** (systemd):
```bash
# Erstelle ~/.config/systemd/user/jellyfin-discord.service
[Unit]
Description=Jellyfin Discord Rich Presence
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/user/jellyfin-discord/main.py
Restart=always
Environment="DISPLAY=:0"

[Install]
WantedBy=default.target

# Aktivieren
systemctl --user enable jellyfin-discord
systemctl --user start jellyfin-discord
```

### Umgebungsvariablen

Zusätzliche Optionen für `.env`:

```env
# Logging (optional)
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR
LOG_FILE=jellyfin-rpc.log   # Dateiname für Logs

# Timing (optional)
UPDATE_INTERVAL=3           # Sekunden zwischen Updates (Standard: 3)
RECONNECT_DELAY=30          # Sekunden vor Reconnect-Versuch

# Rich Presence Anpassungen
SHOW_ALBUM=true            # Album anzeigen (true/false)
SHOW_TIME=true             # Spielzeit anzeigen (true/false)
LARGE_IMAGE=music          # Name des großen Icons
SMALL_IMAGE=play           # Name des kleinen Icons
```

## 🐛 Debugging & Logs

### Debug-Modus aktivieren

1. In `.env` hinzufügen:
   ```env
   LOG_LEVEL=DEBUG
   ```

2. Script neu starten

3. Detaillierte Ausgabe im Terminal beobachten

### Log-Datei analysieren

```bash
# Letzte 50 Zeilen anzeigen
tail -n 50 jellyfin-rpc.log

# Live-Logs verfolgen
tail -f jellyfin-rpc.log

# Nach Fehlern suchen
grep ERROR jellyfin-rpc.log
```

## 🔒 Sicherheit & Privatsphäre

### Best Practices

1. **API Keys schützen**
   - Niemals in öffentlichen Repos committen
   - `.env` in `.gitignore` aufnehmen

2. **Netzwerksicherheit**
   - Nutze HTTPS für externe Jellyfin-Verbindungen
   - VPN für Remote-Zugriff empfohlen

3. **Discord-Privatsphäre**
   - Rich Presence kann von jedem in gemeinsamen Servern gesehen werden
   - In Server-Einstellungen deaktivierbar

### Berechtigungen

Das Script benötigt:
- ✅ Lesezugriff auf Jellyfin-Sessions
- ✅ Discord RPC Zugriff
- ❌ Keine Admin-Rechte
- ❌ Keine Schreibzugriffe

## 📊 Performance & Optimierung

### Ressourcenverbrauch

- **CPU**: < 1% im Durchschnitt
- **RAM**: 30-50 MB
- **Netzwerk**: ~1 KB/s
- **Disk I/O**: Minimal (nur Logs)

### Optimierungstipps

1. **Update-Intervall erhöhen**
   ```env
   UPDATE_INTERVAL=10  # Reduziert API-Calls
   ```

2. **Logs deaktivieren**
   ```env
   LOG_LEVEL=ERROR    # Nur Fehler loggen
   ```

3. **Python-Optimierungen**
   ```bash
   python -O main.py  # Optimized mode
   ```

## ❓ Häufig gestellte Fragen

**F: Kann ich mehrere Instanzen für verschiedene User laufen lassen?**  
A: Ja, aber jede braucht eine eigene Discord App ID und separaten Port.

**F: Funktioniert es mit Plex/Emby?**  
A: Mit Anpassungen ja, da die APIs ähnlich sind.

**F: Warum wird mein Album-Cover nicht angezeigt?**  
A: Discord Rich Presence unterstützt keine dynamischen Bilder.

**F: Kann ich die 3-Sekunden-Verzögerung reduzieren?**  
A: Ja, aber bedenke die API-Rate-Limits von Jellyfin.

**F: Funktioniert es mit Jellyfin-Plugins?**  
A: Ja, solange die Standard-API verwendet wird.

**F: Unterstützt es Playlisten-Anzeige?**  
A: Nein, nur der aktuelle Song wird angezeigt.

## 🆘 Support & Hilfe

### Hilfe bekommen

1. **GitHub Issues**: Für Bugs und Feature-Requests
2. **Jellyfin Forum**: [forum.jellyfin.org](https://forum.jellyfin.org)
3. **Discord Server**: Jellyfin Community Discord

### Logs für Bug-Reports

Wenn du einen Bug meldest, inkludiere:
- Python-Version: `python --version`
- Jellyfin-Version
- Betriebssystem
- Relevante Log-Einträge
- `.env` (OHNE API Keys!)

---

[← Discord Setup](discord-setup.md) | [Zur Hauptseite →](../README.md)