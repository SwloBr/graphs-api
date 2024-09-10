from opencage.geocoder import OpenCageGeocode


class OpenCageService:
    def __init__(self):
        from app.config import Settings
        self.api_key = Settings().opencage_key
        self.geocoder = OpenCageGeocode(self.api_key)

    def get_location(self, location):
        result = self.geocoder.geocode(location)
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        return [lat, lng]
