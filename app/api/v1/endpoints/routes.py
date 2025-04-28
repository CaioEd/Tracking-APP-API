from fastapi import APIRouter, FastAPI, HTTPException, Depends
from app.services.route_service import RouteService
from app.schemas.routes import RouteCreateRequest, RouteResponse
from app.core.database import Database
from typing import List

routes_router = APIRouter(prefix="/api/v1/routes", tags=["routes"])

routes_router.post("/", response_model=RouteResponse)
async def create_route(route: RouteCreateRequest, route_service: RouteService = Depends()):
    try:
        return await route_service.create_route(route)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@routes_router.get("/", response_model=List[RouteResponse])
async def get_routes(route_service: RouteService = Depends()):
    try:
        return await route_service.list_routes()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))