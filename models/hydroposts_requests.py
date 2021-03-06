from pydantic import BaseModel, EmailStr, validator
from fastapi import HTTPException
import re

class CreateHydropostRequest(BaseModel):
    id: int
    post_id: int
    region: str
    river: str
    latitude: float
    longitude: float
    post_type: str

class GetHydropostByRectRequest(BaseModel):
    latitude_from: float
    longitude_from: float
    latitude_to: float
    longitude_to: float
    post_type: str

class Date(BaseModel):
    day: int
    month: int
    year: int


