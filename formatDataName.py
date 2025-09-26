import os
import re
from pathlib import Path


PATH_NAME = "C:/Users/Utilisateur/Downloads/[ OxTorrent.com ] The Big Bang Theory S01 DVDRip/"
folder = Path(PATH_NAME)

# liste uniquement les fichiers
files = [PATH_NAME + file.name for file in folder.iterdir() if file.is_file()]

for filename in files:

    # Expression régulière pour capturer l'épisode (ex: 1x01)
    match = re.search(r'\d+x(\d+)', filename, re.IGNORECASE)
    if match:
        episode = match.group(1).zfill(2)  # ex: "01"
        extension = os.path.splitext(filename)[1]  # récupère ".avi"
        new_name = PATH_NAME + f"{episode}{extension}"
        
        os.rename(filename, new_name)
        print(f"Fichier renommé : {new_name}")
    else:
        print("Impossible de trouver l'épisode dans le nom du fichier.")
