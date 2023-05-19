from pydantic.dataclasses import dataclass


class Config:
    validate_assignment = True


@dataclass(config=Config)
class WorldPopulation:
    world_id: int
    average: int
    nc: int
    tr: int
    vs: int
