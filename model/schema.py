from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.database import Base

class Cat_schema(Base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String)
    location_of_origin = Column(String)
    coat_length = Column(Float)
    body_type = Column(String)
    pattern = Column(String)

