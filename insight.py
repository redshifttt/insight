import json
import requests
import sys
import os

class Insight:
    def __init__(self, results_per_page=100, page=0, start_sol=1, end_sol=5, camera="icc", output_directory="images"):
        # Init defaults in the object
        self.results_per_page = results_per_page
        self.page = page
        self.start_sol = start_sol
        self.end_sol = end_sol
        self.camera = camera
        self.output_directory = output_directory

    def download_images(self):
        while True:
            req = requests.get(f"https://mars.nasa.gov/api/v1/raw_image_items/?order=sol&per_page={self.results_per_page}&page={self.page}&condition_1=insight:mission&condition_2={self.start_sol}:sol:gte&condition_3={self.end_sol}:sol:lte&search={self.camera}&extended=")

            res = json.loads(req.text)
            error_msg = res.get("error_message")
            if error_msg:
                print(f"error: {error_msg}.")
                sys.exit(1)

            is_more = res["more"]
            found_images = res["items"]
            image_urls = [image["url"] for image in found_images]

            for image in image_urls:
                *_, image_sol, camera, filename = image.split("/")

                dir_to_make = os.path.join(self.output_directory, image_sol, camera.upper())
                output_name = os.path.join(dir_to_make, filename)

                os.makedirs(dir_to_make, exist_ok=True)

                response = requests.get(image)
                with open(output_name, 'wb') as f:
                    print("downloading to", output_name)
                    f.write(response.content)

            if is_more:
                self.page += 1
                print(f"Page {self.page + 1}")
                continue
            else:
                print("All done.")
                sys.exit()
