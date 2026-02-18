import torch

from backend.models.gnn_model import TeknocityGNN


def export_pytorch(model: TeknocityGNN, path: str = "teknocity_model.pt") -> None:
    torch.save(model.state_dict(), path)


def export_onnx(model: TeknocityGNN, onnx_path: str, in_channels: int = 4) -> None:
    model.eval()
    x = torch.randn(4, in_channels)
    edge_index = torch.tensor([[0, 1, 2], [1, 2, 3]], dtype=torch.long)
    torch.onnx.export(model, (x, edge_index), onnx_path, input_names=["x", "edge_index"])
