import requests

from core.image_handler import ImageHandler

class Receiver:
    def __init__(self):
        self.receiver_url = "http://ec2-34-219-219-11.us-west-2.compute.amazonaws.com:443/gaugan2_receive_output"
        self.image_handler = ImageHandler()

    def get(self, image_name):
        response = requests.post(
            self.receiver_url,
            data = {"name": image_name},
            headers={"Content-Type":"application/x-www-form-urlencoded"}
        )

        self.image_handler.save(image_name, response.content)

