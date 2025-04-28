from pydantic import BaseModel
from typing import Any

class Route(BaseModel):
    start_location: str
    end_location: str
    route_data: Any  

    class Config:
        orm_mode = True
