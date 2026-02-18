import random
from collections import deque

import torch
import torch.nn as nn
import torch.optim as optim


class DQN(nn.Module):
    def __init__(self, state_size: int, action_size: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_size, 128),
            nn.ReLU(),
            nn.Linear(128, action_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class DQNAgent:
    def __init__(
        self,
        state_size: int,
        action_size: int,
        learning_rate: float = 1e-3,
        gamma: float = 0.99,
        epsilon: float = 1.0,
        epsilon_min: float = 0.05,
        epsilon_decay: float = 0.995,
        memory_size: int = 10_000,
    ):
        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.memory = deque(maxlen=memory_size)

        self.policy = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=learning_rate)
        self.loss_fn = nn.MSELoss()

    def select_action(self, state: torch.Tensor) -> int:
        if random.random() < self.epsilon:
            return random.randrange(self.action_size)
        with torch.no_grad():
            q_values = self.policy(state)
            return int(torch.argmax(q_values).item())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def learn(self, batch_size: int = 32) -> float | None:
        if len(self.memory) < batch_size:
            return None

        batch = random.sample(self.memory, batch_size)
        loss_total = 0.0
        for state, action, reward, next_state, done in batch:
            q_values = self.policy(state)
            with torch.no_grad():
                max_next_q = torch.max(self.policy(next_state)).item()
                target = reward if done else reward + self.gamma * max_next_q
            expected = q_values.clone().detach()
            expected[action] = target

            loss = self.loss_fn(q_values, expected)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            loss_total += float(loss.item())

        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        return loss_total / batch_size
