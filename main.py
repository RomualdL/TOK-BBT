from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import subprocess


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
            subclip.write_videofile(output_path, codec="mpeg4")
        print(f"✅ Vidéo exportée : {output_path}")
    except Exception as e:
        print(f"❌ Erreur : {e}")
        

PATH_NAME = "C:/Users/Utilisateur/Downloads/[ OxTorrent.com ] The Big Bang Theory S01 DVDRip/"

src = PATH_NAME + "01.avi"
des = PATH_NAME + "cc01.avi"

couper_sequence(src,"60","120",des)