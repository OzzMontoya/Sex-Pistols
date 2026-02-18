# Teknocity (Guadalajara Pilot)

Scaffold implementation of the roadmap modules:

- FastAPI backend with ingestion, inference, and websocket endpoints.
- PostgreSQL session wiring via SQLAlchemy async engine.
- Graph builder service (NetworkX).
- GNN model (PyTorch Geometric).
- RL DQN agent and training loop.
- SUMO simulation runner and reward calculator.
- Model export helpers for PyTorch and ONNX.

## Run API

```bash
cd teknocity/backend
uvicorn main:app --reload
```

## Endpoints

- `POST /traffic/update`
- `POST /traffic/inference`
- `GET /health`
- `WS /ws/traffic`
