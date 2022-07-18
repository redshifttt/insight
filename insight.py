# import json
# import requests
import sys

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
        self.API_LINK = self.update_link()

    def set_results_per_page(self, results):
        if not results in (25, 50, 100):
            print("error: please give an accurate amount of results per page. Expecting 25, 50 or 100.")
            sys.exit(1)
        self.results_per_page = results
        self.API_LINK = self.update_link()

    def set_sol_range(self, start=None, end=None):
        # TODO: If start is not none then set the values else fallback to defaults
        self.start_sol = start
        self.end_sol = end
        self.API_LINK = self.update_link()

    def update_link(self):
        return f"https://mars.nasa.gov/api/v1/raw_image_items/?order=sol&per_page={self.results_per_page}&page={self.page}&condition_1=insight:mission&condition_2={self.start_sol}:sol:gte&condition_3={self.end_sol}:sol:lte&search={self.camera}&extended="

insight = Insight()

insight.set_results_per_page(51)
# insight.set_sol_range(1, 200)

print(f"Start sol: {insight.start_sol}\nEnd sol: {insight.end_sol}\nResults per page: {insight.results_per_page}\nAPI Link: {insight.API_LINK}")
