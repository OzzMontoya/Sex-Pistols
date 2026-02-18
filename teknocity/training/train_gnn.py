import torch

from backend.models.gnn_model import TeknocityGNN


def train_step(model: TeknocityGNN, x: torch.Tensor, edge_index: torch.Tensor, y: torch.Tensor) -> float:
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = torch.nn.MSELoss()

    pred = model(x, edge_index)
    loss = criterion(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return float(loss.item())
