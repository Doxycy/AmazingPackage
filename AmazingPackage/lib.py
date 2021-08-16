import matplotlib.pyplot as plt
import numpy as np
#from PIL import Image
from skimage import io


def try_me():
    rep=input("Do you want some Jean-Rémi's nudes ?\n [Y/N]")
    if rep.lower()=='y':
        img = io.imread(
            "http://dominique.billot1.free.fr/site_arts_visuels/site_sculpture_musee/090108%20bonhomme%20file%20de%20fer/modele04.jpg"
        )
        plt.imshow(img)
        plt.axis('off')
        plt.title('Have Fun ;)')
        plt.show()
    else :
        print("You don't know what you are missing")
