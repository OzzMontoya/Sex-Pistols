from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from models.traffic_state import TrafficState


async def store_traffic_state(db: AsyncSession, state: TrafficState) -> dict[str, Any]:
    payload = state.model_dump()
    # Placeholder insert to keep project DB-agnostic while wiring PostgreSQL session.
    await db.execute(text("SELECT 1"))
    await db.commit()
    return payload
