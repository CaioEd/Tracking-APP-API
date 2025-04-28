from pydantic import BaseModel
from typing import List, Optional


class RouteCreateRequest(BaseModel):
    start_location: str
    end_location: str


class RouteResponse(RouteCreateRequest):
    id: str
    route_data: Optional[dict]

    class Config:
        orm_mode = True
