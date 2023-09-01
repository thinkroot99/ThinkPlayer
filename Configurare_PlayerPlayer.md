
# ThinkPlayer - Un player muzical pentru Arch Linux

**Descriere:**

ThinkPlayer este un script Python care funcționează ca un player muzical simplu pentru utilizatorii sistemului de operare Arch Linux. Acesta utilizează biblioteca VLC Python Bindings pentru a controla redarea melodiilor și oferă o interfață de utilizator text pentru gestionarea melodiilor și a redării.

**Dependențe:**

- VLC Python Bindings (`python-vlc`): Necesar pentru controlul redării melodiilor.

**Instalare dependențe:**

Pentru a instala dependența în Arch Linux, utilizați comanda următoare:

    sudo pacman -S python-vlc

**Configurare:**

1. Asigurați-vă că aveți Python instalat. Deschideți un terminal și introduceți `python --version` pentru a verifica versiunea instalată.
2. Asigurați-vă că dependența `python-vlc` este instalată (vezi mai sus).
3. Salvați scriptul într-un fișier cu extensia `.py`, de exemplu `ThinkPlayer.py`.
4. Acordați permisiuni de execuție scriptului folosind comanda: `chmod +x ThinkPlayer.py`
5. Adăugați directorul curent în variabila de mediu PATH pentru a putea rula scriptul fără `./` în fața numelui (vedeți instrucțiunile pentru shell-ul dvs.).

**Utilizare:**

- Rulați scriptul cu comanda: `ThinkPlayer.py`.
- Urmați instrucțiunile din meniu pentru a interacționa cu playerul muzical.
- Melodiile (format MP3 sau M4A) trebuie să fie prezente în directorul specificat în script (`music_directory`).

**Observații:**

- Playerul poate reda formate audio diverse, dar disponibilitatea acestora depinde de codec-uri și dependințe suplimentare.
- Dacă întâmpinați probleme cu anumite formate audio, asigurați-vă că VLC și sistemul dvs. au toate dependințele necesare instalate.

**Autor:**

ThinkRoot99
