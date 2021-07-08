import numpy as np
from PIL import Image

def import_image(path):
    image = Image.open(path).convert('L')
    frame = np.asarray(image)
    image.show()
    return frame

print(import_image('a.PNG'))

