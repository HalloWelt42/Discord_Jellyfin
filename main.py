import warnings

warnings.filterwarnings("ignore", category=UserWarning)

from pypresence import Presence
import requests
import time
import os
from dotenv import load_dotenv

# .env laden
load_dotenv()

JELLYFIN_URL = os.getenv("JELLYFIN_URL")
API_KEY = os.getenv("API_KEY")
USER_ID = os.getenv("USER_ID")
DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
IDLE_TEXT = os.getenv("IDLE_TEXT", "Jellyfin-Player")  # Werbetext mit Fallback

if not all([JELLYFIN_URL, API_KEY, USER_ID, DISCORD_CLIENT_ID]):
    print("❌ Fehler: Eine oder mehrere .env-Variablen fehlen.")
    exit(1)

# Discord verbinden
try:
    rpc = Presence(DISCORD_CLIENT_ID)
    rpc.connect()
    print("✅ Discord Rich Presence verbunden!")
except Exception as e:
    print(f"❌ Fehler beim Verbinden zu Discord: {e}")
    exit(1)


def get_now_playing():
    url = f"{JELLYFIN_URL}/Sessions"
    headers = {"X-Emby-Token": API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            print(f"❌ HTTP-Fehler {response.status_code}: {response.text}")
            return None, None, None

        sessions = response.json()
        for session in sessions:
            if session.get("UserId") == USER_ID and session.get("NowPlayingItem"):
                item = session["NowPlayingItem"]

                # Titel
                title = item.get("Name", "Unbekannter Titel")

                # Album
                album = item.get("Album", "")

                # Künstler - korrigiert für JSON-Objekt
                artists = item.get("AlbumArtists", [])
                if artists and isinstance(artists, list) and len(artists) > 0:
                    # Wenn es ein Dictionary ist, hole den Namen
                    if isinstance(artists[0], dict):
                        artist = artists[0].get("Name", "")
                    else:
                        artist = str(artists[0])
                else:
                    # Fallback auf Artists
                    artists = item.get("Artists", [])
                    if artists and isinstance(artists, list) and len(artists) > 0:
                        if isinstance(artists[0], dict):
                            artist = artists[0].get("Name", "")
                        else:
                            artist = str(artists[0])
                    else:
                        artist = ""

                return title, artist, album

    except Exception as e:
        print("❌ Fehler beim Abrufen der Wiedergabeinformationen:", e)

    return None, None, None


def update_idle_status():
    """Zeigt den Werbetext/Idle-Status an"""
    try:
        rpc.update(
            details=IDLE_TEXT,
            state="Bereit zum Abspielen",
            large_image="music",
            large_text="Jellyfin Music Player"
        )
        print(f"💤 Idle-Status gesetzt: {IDLE_TEXT}")
    except Exception as e:
        print(f"❌ Fehler beim Setzen des Idle-Status: {e}")


def update_playing_status(title, artist, album):
    """Zeigt den aktuell spielenden Song an"""
    try:
        # Status-Text zusammenbauen
        if artist and album:
            state_text = f"{artist} – {album}"
        elif artist:
            state_text = artist
        elif album:
            state_text = album
        else:
            state_text = "Jellyfin Music"

        rpc.update(
            details=title,
            state=state_text,
            large_image="music",
            large_text="Jellyfin",
            small_image="play",
            small_text="Playing",
            start=int(time.time())
        )
        print(f"🎵 Spielt: {title} – {artist} – {album}")
    except Exception as e:
        print(f"❌ Fehler beim Discord Update: {e}")


# Hauptloop
print(f"🚀 Jellyfin Discord Rich Presence gestartet!")
print(f"💬 Idle-Text: {IDLE_TEXT}")
print("=" * 50)

last_title = None
is_playing = False

while True:
    try:
        title, artist, album = get_now_playing()

        if title:
            # Musik läuft
            if not is_playing or title != last_title:
                # Neuer Song oder Status hat sich geändert
                update_playing_status(title, artist, album)
                last_title = title
                is_playing = True
        else:
            # Keine Musik
            if is_playing:
                # War vorher am Spielen, jetzt nicht mehr
                update_idle_status()
                is_playing = False
                last_title = None
            elif last_title is None:
                # Erster Durchlauf oder lange kein Update
                print("⏸️  Warte auf Musik...")
                update_idle_status()
                last_title = ""  # Verhindert wiederholte Meldungen

    except KeyboardInterrupt:
        print("\n👋 Beende Programm...")
        break
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")

    time.sleep(3)  # Alle 5 Sekunden prüfen

# Aufräumen
try:
    rpc.clear()
    rpc.close()
    print("✅ Discord Rich Presence getrennt.")
except:
    pass