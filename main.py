from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import subprocess,json


def couper_sequence(video_path, start_time, end_time, output_path):
    """
    Coupe une séquence d'une vidéo entre start_time et end_time.

    Args:
        video_path (str): Chemin de la vidéo source.
        start_time (float): Temps de début en secondes.
        end_time (float): Temps de fin en secondes.
        output_path (str): Chemin du fichier de sortie.
    """
    try:
        with VideoFileClip(video_path) as clip:
            subclip = clip.subclip(start_time, end_time)
            subclip.write_videofile(output_path, codec="libx264")
        print(f"✅ Vidéo exportée : {output_path}")
    except Exception as e:
        print(f"❌ Erreur : {e}")
        
def jsonData(jsonFile):
    with open(jsonFile, "r", encoding="utf-8") as f:
        return json.load(f)
        
        
MY_DATA = jsonData("BBT.json")
SRC_PATH_NAME = "D:/RAA/DATA/BBT/Original/"
DES_PATH_NAME = "D:/RAA/DATA/BBT/TOK/"

for id_episode, items in MY_DATA.items():
    saison = id_episode.split("X")[0]
    episode = id_episode.split("X")[1]
    SRC_NAME = SRC_PATH_NAME + f"S{saison}/"
    for type_video, item in items.items():
        src = SRC_NAME + f"{episode}.avi"
        des = DES_PATH_NAME + f"{episode}X{type_video}.avi"
        couper_sequence(src,item[0],item[1],des)



#couper_sequence(src,"60","120",des)