# Jellyfin API Key einrichten 🔑

Diese Anleitung zeigt dir, wie du einen API Key für Jellyfin erstellst und deine User ID findest.

## 📋 Voraussetzungen

- Jellyfin Server läuft (Version 10.7+)
- Admin-Zugang zu Jellyfin
- Webbrowser

## 🔐 API Key erstellen

### Methode 1: Über die Weboberfläche (Empfohlen)

1. **Jellyfin Web-Interface öffnen**
   - Navigiere zu `http://dein-server:8096` (oder deine Jellyfin URL)
   - Melde dich mit einem Admin-Account an

2. **Zu den Einstellungen navigieren**
   - Klicke auf das **Zahnrad-Symbol** (⚙️) oben rechts
   - Wähle **Dashboard**

3. **API Keys verwalten**
   - Im linken Menü: **Erweitert** → **API-Schlüssel**
   - Klicke auf **"Neuer API-Schlüssel"** (grüner Button)

4. **API Key erstellen**
   - **App-Name**: `Discord Rich Presence` (oder beliebig)
   - Klicke auf **"OK"**
   - **WICHTIG**: Kopiere den angezeigten Key sofort! Er wird nur einmal angezeigt.

5. **Key in .env eintragen**
   ```env
   API_KEY=dein_kopierter_api_key_hier
   ```

### Methode 2: Über die Jellyfin App

Wenn du die Jellyfin Mobile/Desktop App nutzt:

1. In der App einloggen
2. Einstellungen → Entwickler → API Key generieren
3. Key kopieren und in `.env` eintragen

## 🆔 User ID finden

### Option A: Über das Web-Interface

1. **Benutzerverwaltung öffnen**
   - Dashboard → **Benutzer**
   - Klicke auf deinen Benutzernamen

2. **URL prüfen**
   - Schau in die Adresszeile deines Browsers
   - Die URL sieht so aus: `.../dashboard/users/profile?userId=DEINE_USER_ID`
   - Kopiere die lange Zeichenkette nach `userId=`

### Option B: Über die API

1. **Browser öffnen** und navigiere zu:
   ```
   http://dein-server:8096/Users?api_key=DEIN_API_KEY
   ```

2. **Deinen Benutzer finden**
   ```json
   {
     "Name": "DeinBenutzername",
     "Id": "a1b2c3d4e5f6..."  // Das ist deine User ID!
   }
   ```

3. **ID kopieren** und in `.env` eintragen:
   ```env
   USER_ID=a1b2c3d4e5f6...
   ```

## ✅ Konfiguration testen

### Test-URL aufrufen

Teste ob alles funktioniert:
```
http://dein-server:8096/Sessions?api_key=DEIN_API_KEY
```

Du solltest ein JSON-Array sehen (kann leer sein wenn nichts abgespielt wird).

### Häufige Fehler

| Fehler | Lösung |
|--------|---------|
| 401 Unauthorized | API Key ist falsch oder ungültig |
| 404 Not Found | Jellyfin URL ist falsch |
| Connection refused | Jellyfin läuft nicht oder Port ist falsch |
| Leere Session | Spiele Musik ab und teste erneut |

## 🔒 Sicherheitshinweise

1. **API Key geheim halten**
   - Teile niemals deinen API Key
   - Committe die `.env` Datei nicht in Git

2. **Beschränkte Rechte**
   - Der API Key hat die gleichen Rechte wie der erstellende User
   - Erstelle ggf. einen separaten User nur für Discord

3. **HTTPS verwenden**
   - Bei externem Zugriff nutze HTTPS
   - Beispiel: `https://jellyfin.deinedomain.de`

## 🌐 Remote-Zugriff

Wenn dein Jellyfin Server nicht lokal läuft:

1. **Port-Forwarding** (Router)
   - Leite Port 8096 weiter
   - Oder nutze einen Reverse Proxy

2. **DynDNS/Domain**
   - Nutze eine feste Domain
   - Update die JELLYFIN_URL entsprechend

3. **VPN** (Sicherste Option)
   - Verbinde dich per VPN zu deinem Heimnetz
   - Nutze dann die lokale IP

## ❓ FAQ

**F: Kann ich mehrere API Keys haben?**  
A: Ja! Du kannst beliebig viele Keys erstellen und einzeln widerrufen.

**F: Funktioniert es mit Jellyfin-Forks?**  
A: Ja, sollte mit Emby und anderen Forks funktionieren.

**F: Muss ich Admin sein?**  
A: Nur für die API Key Erstellung. Die User ID kannst du auch als normaler User finden.

---

[← Zurück zur Hauptseite](../README.md) | [Discord Setup →](discord-setup.md)