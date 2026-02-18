from typing import Dict

from pydantic import BaseModel, Field


class TrafficState(BaseModel):
    intersection_id: str = Field(..., description="Unique intersection identifier")
    queues: Dict[str, float] = Field(default_factory=dict)
    velocities: Dict[str, float] = Field(default_factory=dict)
    current_phase: str
    timestamp: float
