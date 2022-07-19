import json
import requests
import sys
import os

class Insight:
    # Sane defaults
    _results_per_page: int = 100
    _page: int = 0
    _start_sol: int = 1
    _end_sol: int = 5
    _camera: str = "idc"
    _image_directory: str = "images"

    def __init__(self):
        # Init defaults in the object
        self.results_per_page = Insight._results_per_page
        self.page = Insight._page
        self.start_sol = Insight._start_sol
        self.end_sol = Insight._end_sol
        self.camera = Insight._camera
        self.image_directory = Insight._image_directory
        self.API_LINK = self.update_link()

    def download_images(self):
        r = requests.get(self.API_LINK)
        res = json.loads(r.text)
        if res.get("error_message"):
            print("error: incorrect input values.")
            sys.exit(1)

        is_more = res["more"] # Will always be either True or False
        found_images = res["items"]
        image_urls = [image["url"] for image in found_images]
        page_total_images = str(len(image_urls))
        counter = 1

        for i in image_urls:
            image_sol = i.split("/")[6]
            filename = i.split("/")[8]
            camera = self.camera.upper()
            dir_to_make = os.path.join(self.image_directory, image_sol, camera)

            os.makedirs(dir_to_make, exist_ok=True)

            response = requests.get(i)
            with open(os.path.join(dir_to_make, filename), 'wb') as f:
                print("downloading to", os.path.join(dir_to_make, filename))
                f.write(response.content)
                counter += 1

    def set_save_directory(self, directory=None):
        self.image_directory = directory

    def set_results_per_page(self, results=None):
        if not results in (25, 50, 100):
            print("error: please give an accurate amount of results per page. expecting 25, 50 or 100.")
            sys.exit(1)

        self.results_per_page = results
        self.API_LINK = self.update_link()

    def set_sol_range(self, start=None, end=None):
        self.start_sol = start
        self.end_sol = end
        self.API_LINK = self.update_link()

    def set_camera(self, camera=None):
        self.camera = camera
        self.API_LINK = self.update_link()

    def update_link(self):
        return f"https://mars.nasa.gov/api/v1/raw_image_items/?order=sol&per_page={self.results_per_page}&page={self.page}&condition_1=insight:mission&condition_2={self.start_sol}:sol:gte&condition_3={self.end_sol}:sol:lte&search={self.camera}&extended="

