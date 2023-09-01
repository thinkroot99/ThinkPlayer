#!/usr/bin/env python

"""
ThinkPlayer - Un player muzical pentru Arch Linux.

Dependențe:
- VLC Python Bindings (`python-vlc`): Necesar pentru controlul redării melodiilor.

Pentru a instala dependența în Arch Linux, folosiți următoarea comandă:
sudo pacman -S python-vlc

Utilizare:
1. Asigurați-vă că aveți Python instalat. Deschideți un terminal și introduceți `python --version` pentru a verifica versiunea instalată.
2. Asigurați-vă că dependența `python-vlc` este instalată (vezi mai sus).
3. Salvați acest script într-un fișier cu extensia `.py`, de exemplu `ThinkPlayer.py`.
4. Dacă nu aveți deja permisiuni de execuție, acordați-le folosind comanda: `chmod +x ThinkPlayer.py`

Pentru a putea rula scriptul fără a adăuga `./` în fața numelui, urmați pașii de mai jos pentru a adăuga directorul curent în variabila de mediu PATH:

Pentru bash:
5. Deschideți fișierul de configurare ~/.bashrc într-un editor de text: `nano ~/.bashrc`
6. Adăugați următoarea linie la finalul fișierului: `export PATH=$PATH:$(pwd)`
7. Salvați fișierul și rulați comanda: `source ~/.bashrc`

Pentru zsh:
5. Deschideți fișierul de configurare ~/.zshrc într-un editor de text: `nano ~/.zshrc`
6. Adăugați următoarea linie la finalul fișierului: `export PATH=$PATH:$(pwd)`
7. Salvați fișierul și rulați comanda: `source ~/.zshrc`

După această configurare, puteți rula scriptul direct cu comanda: `ThinkPlayer.py`.
Urmați instrucțiunile din meniul afișat pentru a interacționa cu playerul muzical.

Vă rugăm să aveți în vedere că disponibilitatea redării anumitor formate audio depinde de codec-uri și dependințe suplimentare. În cazul în care întâmpinați probleme cu anumite formate, asigurați-vă că VLC și sistemul dvs. au toate dependințele necesare instalate.

Asigurați-vă că aveți melodii valide (MP3 sau M4A) în directorul specificat în scriptul de mai jos (`music_directory`).

Autor: ThinkRoot99
"""

import os
import glob
import random
import vlc

class MusicPlayer:
    def __init__(self, music_directory):
        self.music_directory = music_directory
        self.playlist = []
        self.current_track_index = 0
        self.instance = vlc.Instance("--no-xlib")
        self.player = self.instance.media_player_new()
        
        # Înregistrare handler eveniment endReached
        events = self.player.event_manager()
        events.event_attach(vlc.EventType.MediaPlayerEndReached, self.next_track)

    def load_music(self):
        audio_files = glob.glob(os.path.join(self.music_directory, '*.mp3')) + glob.glob(os.path.join(self.music_directory, '*.m4a'))
        self.playlist = audio_files

    def play(self):
        if self.playlist:
            current_track = self.playlist[self.current_track_index]
            media = self.instance.media_new(current_track)
            self.player.set_media(media)
            self.player.play()

    def stop(self):
        self.player.stop()

    def next_track(self, event=None):
        self.stop()
        if self.current_track_index < len(self.playlist) - 1:
            self.current_track_index += 1
        else:
            self.current_track_index = 0
        self.play()


    def previous_track(self):
        self.stop()
        if self.current_track_index > 0:
            self.current_track_index -= 1
        else:
            self.current_track_index = len(self.playlist) - 1
        self.play()

    def list_tracks(self):
        print("\nLista melodiilor:")
        for index, track in enumerate(self.playlist):
            print(f"{index + 1}. {os.path.basename(track)}")

    def play_random(self):
        self.stop()
        random.shuffle(self.playlist)
        self.current_track_index = 0
        self.play()

if __name__ == "__main__":
    music_directory = "/home/thinkroot99/Music/audio/"
    player = MusicPlayer(music_directory)
    player.load_music()

    while True:
        os.system("clear")  # Pentru Linux / macOS
        # os.system("cls")  # Pentru Windows

        if player.player.get_state() == vlc.State.Playing:
            print("Redare:", os.path.basename(player.playlist[player.current_track_index]))

        print("\nMeniu:")
        print("1. Reda")
        print("2. Urmatoarea melodie")
        print("3. Melodie anterioara")
        print("4. Redare aleatorie")
        print("5. Lista melodii")
        print("6. Iesire")

        alegere = input("Selecteaza o optiune: ")

        if alegere == "1":
            player.play()
        elif alegere == "2":
            player.next_track()
        elif alegere == "3":
            player.previous_track()
        elif alegere == "4":
            player.play_random()
        elif alegere == "5":
            player.list_tracks()
            input("Apasa Enter pentru a continua...")
        elif alegere == "6":
            break
