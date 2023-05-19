from pydantic.dataclasses import dataclass


class Config:
    validate_assignment = True


@dataclass(config=Config)
class WorldZones:
    """Stores zone states (default state is 'closed')"""
    world_id: int
    amerish: str = 'closed'
    esamir: str = 'closed'
    hossin: str = 'closed'
    indar: str = 'closed'
    oshur: str = 'closed'
