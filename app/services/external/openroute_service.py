import openrouteservice
from openrouteservice import Client

from app.config import Settings
from app.services import IndustryService


class OpenRouteService:

    def __init__(self):
        self.api_key = Settings().openroute_key

    def get_route(self, lat, lng):
        client: Client = openrouteservice.Client(key=self.api_key)

        industry_service = IndustryService()

        actual_coords = [lng, lat]

        locations = industry_service.get_all_industry_coordinates()
        locations.insert(0, actual_coords)

        print(locations)

        profile = "driving-hgv"
        metrics = ["distance", "duration"]
        units = 'km'
        resolve_locations = False

        response = client.distance_matrix(
            locations=locations,
            profile=profile,
            metrics=metrics,
            units=units,
            resolve_locations=resolve_locations)

        durations = response["durations"][0][1:]
        distances = response["distances"][0][1:]

        sub = [durations, distances]
        return sub