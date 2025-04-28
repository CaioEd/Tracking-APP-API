from app.repositories.routes import RouteRepository
from app.core.config import GoogleMapsAPI
from app.domain.models.routes import Route
from app.schemas.routes import RouteCreateRequest
from typing import List


class RouteService:
    def __init__(self):
        self.repository = RouteRepository()
        self.google_maps_api = GoogleMapsAPI()


    async def create_route(self, route_data: RouteCreateRequest) -> Route:
        # Chamando a API do Google Maps para obter os dados da rota
        route_info = self.google_maps_api.get_route(route_data.start_location, route_data.end_location)
        
        # Criando o objeto Route
        route = Route(
            start_location=route_data.start_location,
            end_location=route_data.end_location,
            route_data=route_info
        )
        
        # Salvando a rota no banco de dados
        saved_route = await self.repository.save_route(route)
        return saved_route


    async def list_routes(self) -> List[Route]:
        return await self.repository.get_all_routes()