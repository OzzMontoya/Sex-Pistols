from dataclasses import dataclass


@dataclass(slots=True)
class ScenarioConfig:
    name: str
    intersections: int
    roads: int
    demand_level: str = "medium"


def build_default_scenario() -> ScenarioConfig:
    return ScenarioConfig(name="guadalajara-pilot", intersections=25, roads=40)
