from app.dto.generalDTO import GeneralDTO
from app.dto.responseDTO import ResponseDTO, ResponseTruckDTO
from app.models import Industry
from app.services import IndustryService, TruckService


class GeneralService:

    def execute(self, lat, lng, tons):
        data = self.get_data(lat, lng, tons)

        data = sorted(data, key=lambda x: x.balance)

        selected = data[0]
        industry_service = IndustryService()
        industry = industry_service.get_industry_by_id(selected.enterprise_id)
        truck_service = TruckService(industry_service.db)
        truck = truck_service.get_truck_by_id(selected.truck_id)

        response_truck = ResponseTruckDTO(
            name=truck.name,
            max_tons=truck.max_tons,
            axles=truck.axles,
            km_per_fuel=truck.km_per_fuel,
        )

        response = ResponseDTO(
            enterprise=industry.name,
            distance=selected.distance,
            time=(selected.time/3600),
            cost=selected.cost,
            earnings=selected.earnings,
            profit=selected.profit,
            truck=response_truck)

        return response

    def get_data(self, lat, lng, tons):
        from app.services.external.openroute_service import OpenRouteService
        routes = OpenRouteService().get_route(lat, lng)
        duration = routes[0]
        distance = routes[1]

        industry_service = IndustryService()
        industries = industry_service.get_all_industries()

        truck_service = TruckService(industry_service.db)
        trucks = truck_service.get_trucks()

        general_list = []

        for i in range(len(industries)):
            for j in range(len(trucks)):
                industry = industries[i]
                enterprise_id = industry.id
                truck = trucks[j]
                truck_id = truck.id
                time = duration[i]
                dist = distance[i]

                print(f"Industry: {industry.name} - Truck: {truck.name} - Time: {time} - Distance: {dist}")

                truck_efficiency = truck.km_per_fuel
                fuel_price = truck.fuel.price

                industry_ton_cost = industry.price

                if truck.max_tons < tons:
                    continue
                if time > 3600 * 48:
                    continue

                fuel_cost = (dist / truck_efficiency) * fuel_price
                sugar_revenue = industry.price * tons

                balance = self.total_calc(time, dist, truck_efficiency, fuel_price, industry_ton_cost, tons)
                row = GeneralDTO(
                    enterprise_id=enterprise_id,
                    truck_id=truck_id,
                    distance=dist,
                    time=time,
                    cost=fuel_cost,
                    earnings=sugar_revenue,
                    profit=sugar_revenue - fuel_cost,
                    balance=balance
                )
                general_list.append(row)
        return general_list

    def total_calc(self, time, distance, truck_efficiency, fuel_price, industry_ton_cost, tons_quantity):
        fuel_cost = (distance / truck_efficiency) * fuel_price
        value = (0.5 * time) + (0.3 * distance) + (0.4 * fuel_cost) - (0.2 * (industry_ton_cost * tons_quantity))
        return value
