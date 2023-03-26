"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base
from datetime import datetime


class Planet_(Base):
    """Pydantic model class meant to validate the data for `Planet` object from
    single resource endpoint from starwars API.
    """

    # attribute fields
    planet_id: int
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str


class PatchPlanet(Base):
    planet_id: Optional[int]
    name: Optional[str]
    rotation_period: Optional[str]
    orbital_period: Optional[str]
    diameter: Optional[str]
    climate: Optional[str]
    gravity: Optional[str]
    terrain: Optional[str]
    surface_water: Optional[str]
    population: Optional[str]
    residents: Optional[List[str]]
    films: Optional[List[str]]
