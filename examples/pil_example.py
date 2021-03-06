from ggb import GGB, ColorSpace

import cv2
try:
    import urllib.request as urllib
except:
    import urllib
import numpy as np

from PIL import Image


def main():
    # Load image from internet
    req = urllib.urlopen('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes.png')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    # Converting to GGB Color
    img = Image.fromarray(img)
    ggb_image = GGB(image=img, input_color=ColorSpace.BGR).process()
    ggb_image.show()

    # Result
    img = ggb_image.write()
    img.show()


if __name__ == '__main__':
    main()
