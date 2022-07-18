# import json
# import requests

class Insight:
    # Sane defaults
    _results_per_page: int = 100
    _page: int = 0
    _start_sol: int = 1
    _end_sol: int = 5
    _camera: str = "idc"

    def __init__(self):
        # Init defaults in the object
        self.results_per_page = Insight._results_per_page
        self.page = Insight._page
        self.start_sol = Insight._start_sol
        self.end_sol = Insight._end_sol
        self.camera = Insight._camera
        self.API_LINK: str = f"https://mars.nasa.gov/api/v1/raw_image_items/?order=sol&per_page={self.results_per_page}&page={self.page}&condition_1=insight:mission&condition_2={self.start_sol}:sol:gte&condition_3={self.end_sol}:sol:lte&search={self.camera}&extended="

        print(self.results_per_page)

insight = Insight()
