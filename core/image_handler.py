import os
import datetime

class ImageHandler:
    def __init__(self):
        self.input_images_dir = os.path.abspath("./input_images")
        self.output_images_dir = os.path.abspath("./output_images")

    def generate_name(self, image_name):
        date = self._get_current_date()
        return "{}_{}".format(date, image_name)

    def _get_current_date(self):
        raw_date = datetime.datetime.now()
        formated_date = raw_date.strftime("%Y-%m-%d")
        return formated_date

    def get_image_paths(self):
        for filename in os.listdir(self.input_images_dir):
            file_path = os.path.join(self.input_images_dir, filename)
            if os.path.isfile(file_path):
                yield file_path

    def save(self, image_name, image_content):
        output_image_path = os.path.join(self.output_images_dir, image_name)
        with open(output_image_path, "wb") as output:
            output.write(image_content)

    def delete(self, image_path):
        os.remove(image_path)