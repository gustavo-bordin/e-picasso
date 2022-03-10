import base64
import os

from core.image_handler import ImageHandler
from core.inferer import Inferer
from core.receiver import Receiver


class Picasso:
    def __init__(self):
        self.image_handler = ImageHandler()
        self.inferer = Inferer()
        self.receiver = Receiver()

        self._insert_draw()

    def _insert_draw(self):
        image_paths = self.image_handler.get_image_paths()

        for image_path in image_paths:
            with open(image_path, "rb") as image:
                image_b64 = base64.b64encode(image.read())
                raw_image_name = os.path.basename(image_path)
                formated_image_name = self.image_handler.generate_name(raw_image_name)
                response = self.inferer.post(formated_image_name, image_b64)
                if response.get("success") == True:
                    self.receiver.get(formated_image_name)
                    self.image_handler.delete(image_path)


picasso = Picasso()