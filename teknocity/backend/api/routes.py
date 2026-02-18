from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
import torch

from database import get_db
from models.gnn_model import TeknocityGNN
from models.traffic_state import TrafficState
from services.data_ingestion import store_traffic_state
from services.prediction_service import predict_congestion

router = APIRouter()


class InferenceRequest(BaseModel):
    node_features: list[list[float]]
    edge_index: list[list[int]]


@router.post("/traffic/update")
async def update_traffic(data: TrafficState, db: AsyncSession = Depends(get_db)):
    stored = await store_traffic_state(db, data)
    return {"status": "ok", "data": stored}


@router.post("/traffic/inference")
async def infer_congestion(payload: InferenceRequest):
    x = torch.tensor(payload.node_features, dtype=torch.float32)
    edge_index = torch.tensor(payload.edge_index, dtype=torch.long)
    model = TeknocityGNN(in_channels=x.shape[1], hidden=16, out_channels=1)
    pred = predict_congestion(model, x, edge_index)
    return {"predictions": pred.squeeze(-1).tolist()}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}
