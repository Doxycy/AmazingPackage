import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from PIL import Image

def try_me():
    rep=input("Do you want some Jean-Rémi's nudes ?\n [Y/N]")
    if rep.lower()=='y':
        chem=os.path.abspath(sys.path[0])
        chem=os.path.join(chem,"JR.jpeg")
        img = np.array(Image.open(chem))
        plt.imshow(img)
        plt.axis('off')
        plt.title('Have Fun ;)')
        plt.show()
    print("You don't know what you are missing")
