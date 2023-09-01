
# Player Muzical pentru Arch Linux folosind API-ul VLC și Python

## Dependențe și Configurare:

- Scriptul necesită biblioteca `python-vlc` pentru a controla redarea melodiilor prin VLC. Puteți instala dependența folosind comanda:

    sudo pacman -S python-vlc


- Salvați scriptul cu extensia `.py`, de exemplu `ThinkPlayer.py`.
- Asigurați-vă că directorul curent este adăugat la variabila de mediu `PATH`, astfel încât să puteți rula scriptul fără a folosi `./` în fața numelui acestuia.

## Clasa `MusicPlayer`:

Clasa `MusicPlayer` gestionează funcționalitatea playerului muzical.

- În constructorul clasei se inițializează:
- Calea către directorul de muzică (`music_directory`)
- Lista de melodii (`playlist`)
- Indexul melodiei curente (`current_track_index`)
- Instanța VLC (`instance`)
- Playerul VLC (`player`)
- Se înregistrează un handler pentru evenimentul `MediaPlayerEndReached`, astfel încât să se treacă automat la următoarea melodie după ce melodia curentă se termină.

## Funcții de Control al Redării:

- `load_music()`: Încarcă melodii din directorul specificat și le adaugă în playlist.
- `play()`: Selectează melodia curentă din playlist, creează o instanță media VLC și pornește redarea.
- `stop()`: Oprește redarea curentă.
- `next_track()`: Trece la următoarea melodie din playlist și pornește redarea acesteia.
- `previous_track()`: Trece la melodia anterioară din playlist și pornește redarea acesteia.
- `list_tracks()`: Afișează lista de melodii din playlist.
- `play_random()`: Amestecă playlist-ul și pornește redarea melodiei curente din playlist amestecat.

## Secțiunea Principală (`__name__ == "__main__"):

- Se configurează calea către directorul de muzică (`music_directory`) și se creează o instanță a clasei `MusicPlayer`.
- Se încarcă melodiile din directorul specificat în playlist.
- Se afișează un meniu pentru interacțiunea cu playerul, permițând utilizatorului să redă, să treacă la următoarea sau anterioara melodie, să redă aleatoriu, să afișeze lista de melodii sau să iasă din aplicație.

În general, acest script oferă o modalitate simplă de a reda și gestiona melodiile dintr-un director specificat utilizând VLC Python Bindings. Utilizatorul poate interacționa cu playerul prin intermediul unui meniu text, alegând diferite opțiuni pentru controlul redării melodiilor.
