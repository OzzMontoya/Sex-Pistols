import torch

from models.gnn_model import TeknocityGNN


def predict_congestion(
    model: TeknocityGNN,
    node_features: torch.Tensor,
    edge_index: torch.Tensor,
) -> torch.Tensor:
    model.eval()
    with torch.no_grad():
        return model(node_features, edge_index)
