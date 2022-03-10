import requests

from core.image_handler import ImageHandler

class Inferer:
    def __init__(self):
        self.inferer_url = "http://ec2-34-219-219-11.us-west-2.compute.amazonaws.com:443/gaugan2_infer"
        self.image_handler = ImageHandler()

    def post(self, image_name, image_b64):
        response = requests.post(
            self.inferer_url, 
            data = {
                "name": image_name,
                "masked_segmap": image_b64,
                "style_name": "random",
                "caption": "",
                "enable_seg": True,
                "enable_edge": False,
                "enable_caption": False,
                "enable_image": False,
                "use_model2": False,
            }
        )

        return response.json()

