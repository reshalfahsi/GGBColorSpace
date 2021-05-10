from ggb.utils.constant import ColorSpace, CVLib
from ggb.utils.error import ColorSpaceError

import numpy as np

class GGBImage(object):
    """Image handler for GGB.
    
    :param image: image source either from path or variable
    :param backend: computer vision library which handle the task
    """
    def __init__(self, image=None, backend=CVLib.OPENCV):
        self.__backend = backend
        self.__image = self.read(image, backend)


    def backend(self):
        """Check which computer vision library is used as backend
        
        :return: type of computer vision library
        """
        return self.__backend


    def read(self, source, backend=CVLib.OPENCV):
        """Read image from source.
    
        :param source: image source either from path or variable
        :param backend: computer vision library which handle the task
        :return: image variable
        """
        if isinstance(source, str):
            if backend == CVLib.OPENCV:
                self.__backend = CVLib.OPENCV
                import cv2
                return cv2.imread(path)
            else:
                self.__backend = CVLib.PIL
                from PIL import Image
                return Image.open(path).convert('RGB')
        else:
            if isinstance(source, np.ndarray):
                self.__backend = CVLib.OPENCV
            else:
                self.__backend = CVLib.PIL
            return source


    def write(self, path=None):
        """Write the image into a file when path is not None 
           or variable when path is None.
         
        :param path: path to file
        """
        if path == None:
            return self.__image
        else:
            if self.__backend == CVLib.OPENCV:
                import cv2
                self.__image = self.__image.astype('uint8')
                cv2.imwrite(path, self.__image)
            else:
                self.__image.save(path)


    def show(self):
        """Show the image.
        """
        if self.__backend == CVLib.OPENCV:
            import cv2
            self.__image = self.__image.astype('uint8')
            cv2.imshow("GGB", self.__image)
            cv2.waitKey(0)
        else:
            self.__image.show()
