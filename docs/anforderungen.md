# Anforderungsanalyse: Jellyfin Discord Rich Presence

## 1. Projektziel

Entwicklung einer Python-Anwendung, die den aktuellen Musikstatus von Jellyfin Media Server automatisch als Discord Rich Presence anzeigt, um Freunden und Community-Mitgliedern zu zeigen, welche Musik gerade gehört wird.

## 2. Funktionale Anforderungen

### 2.1 Kernanforderungen

- **FA01**: Automatische Erkennung von Musik, die über Jellyfin abgespielt wird
- **FA02**: Echtzeitübertragung von Songinformationen an Discord Rich Presence
- **FA03**: Anzeige von Titel, Künstler und Album im Discord-Status
- **FA04**: Automatische Aktualisierung bei Songwechsel (max. 5 Sekunden Verzögerung)
- **FA05**: Idle-Status mit benutzerdefiniertem Text bei Inaktivität

### 2.2 Konfigurationsanforderungen

- **FA06**: Konfiguration über Umgebungsvariablen (.env-Datei)
- **FA07**: Unterstützung für lokale und remote Jellyfin-Server
- **FA08**: Anpassbare Update-Intervalle
- **FA09**: Optionaler Werbetext für Idle-Modus

### 2.3 Benutzeroberfläche

- **FA10**: Kommandozeilen-Interface (CLI)
- **FA11**: Echtzeit-Statusmeldungen im Terminal
- **FA12**: Graceful Shutdown über Ctrl+C

## 3. Nicht-funktionale Anforderungen

### 3.1 Leistungsanforderungen

- **NFA01**: Maximale CPU-Auslastung < 5%
- **NFA02**: RAM-Verbrauch < 100 MB
- **NFA03**: Netzwerktraffic < 10 KB/s
- **NFA04**: Reaktionszeit für Updates < 5 Sekunden

### 3.2 Kompatibilität

- **NFA05**: Python 3.7+ Unterstützung
- **NFA06**: Plattformunabhängig (Windows, macOS, Linux)
- **NFA07**: Jellyfin Server 10.7+
- **NFA08**: Discord Desktop Client (keine Browser-Unterstützung)

### 3.3 Sicherheit

- **NFA09**: Sichere Speicherung von API-Credentials
- **NFA10**: Keine Klartext-Passwörter im Code
- **NFA11**: Unterstützung für HTTPS-Verbindungen
- **NFA12**: Minimale Berechtigungen (nur Lese-Zugriff)

### 3.4 Zuverlässigkeit

- **NFA13**: Automatische Wiederverbindung bei Verbindungsabbruch
- **NFA14**: Fehlerbehandlung für API-Timeouts
- **NFA15**: Graceful Degradation bei fehlenden Metadaten

### 3.5 Wartbarkeit

- **NFA16**: Modularer Code-Aufbau
- **NFA17**: Ausführliche Dokumentation
- **NFA18**: Logging-Funktionalität für Debugging
- **NFA19**: Versionskontrolle mit Git

## 4. Technische Anforderungen

### 4.1 Abhängigkeiten

- **Python-Pakete**:
  - pypresence (Discord RPC)
  - requests (HTTP-Requests)
  - python-dotenv (Umgebungsvariablen)

### 4.2 APIs

- **Jellyfin REST API**: Session-Endpunkt für Wiedergabeinformationen
- **Discord RPC**: Rich Presence Protocol über IPC

### 4.3 Datenfluss

1. Polling der Jellyfin Sessions API alle 5 Sekunden
2. Extraktion der Musikmetadaten aus der Antwort
3. Formatierung der Daten für Discord Rich Presence
4. Update des Discord-Status über pypresence

## 5. Einschränkungen

- Keine Unterstützung für Video-Content
- Keine Multi-User-Funktionalität
- Keine Album-Cover in Discord (API-Limitation)
- Abhängigkeit von Discord Desktop Client

## 6. Risiken & Mitigationen

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|---------|------------|
| API-Änderungen | Mittel | Hoch | Versionsprüfung, Community-Support |
| Rate-Limiting | Niedrig | Mittel | Konfigurierbares Polling-Intervall |
| Verbindungsabbrüche | Mittel | Niedrig | Auto-Reconnect-Mechanismus |
| Credential-Leak | Niedrig | Hoch | .gitignore, Dokumentation |

## 7. Erfolgskriterien

- ✅ Musik wird innerhalb von 5 Sekunden in Discord angezeigt
- ✅ Stabile Ausführung über 24+ Stunden
- ✅ Einfache Installation in < 10 Minuten
- ✅ CPU-Auslastung bleibt unter 5%
- ✅ Funktioniert auf allen drei Hauptplattformen

## 8. Zukünftige Erweiterungen

- GUI-Interface (Optional)
- Discord-Bot-Integration
