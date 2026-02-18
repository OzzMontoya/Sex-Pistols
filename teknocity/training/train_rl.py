import torch

from backend.models.rl_agent import DQNAgent


def run_training_loop(env, episodes: int = 1_000):
    agent = DQNAgent(state_size=env.state_size, action_size=env.action_size)

    for _ in range(episodes):
        state = torch.tensor(env.reset(), dtype=torch.float32)
        done = False

        while not done:
            action = agent.select_action(state)
            next_state_raw, reward, done = env.step(action)
            next_state = torch.tensor(next_state_raw, dtype=torch.float32)
            agent.remember(state, action, reward, next_state, done)
            agent.learn()
            state = next_state

    return agent
