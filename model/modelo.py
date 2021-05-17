from pydantic import BaseModel
from typing import List, Optional

class Cat_model(BaseModel):
    breed : str
    location_of_origin : str
    coat_length : float
    body_type : str
    pattern : str

class Show_cat(BaseModel):
    id: int
    breed : str
    location_of_origin : str
    coat_length : float
    body_type : str
    pattern : str
    class Config():
        orm_mode = True

class Filter_cat(BaseModel):
    breed : Optional[str]
    location_of_origin : Optional[str]
    coat_length : Optional[float]
    body_type : Optional[str]
    pattern : Optional[str]