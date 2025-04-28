from app.core.database import db
from app.domain.models.routes import Route
from app.schemas.routes import RouteResponse
from bson import ObjectId
from typing import List


class RouteRepository:
    def __init__(self):
        self.collection = db.db.routes  # Definindo a coleção 'routes' no banco MongoDB


    async def save_route(self, route: Route) -> RouteResponse:
        result = await self.collection.insert_one(route.model_dump())  # Usando model_dump()
        route_id = str(result.inserted_id)
        return RouteResponse(id=route_id, **route.model_dump())  # Usando model_dump()


    async def get_all_routes(self) -> List[RouteResponse]:
        routes = await self.collection.find().to_list(100)
        return [RouteResponse(id=str(route["_id"]), **route) for route in routes]
