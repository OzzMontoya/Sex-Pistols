import torch


def evaluate_policy(agent, env, episodes: int = 10) -> float:
    rewards = []
    for _ in range(episodes):
        state = torch.tensor(env.reset(), dtype=torch.float32)
        done = False
        total_reward = 0.0
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            state = torch.tensor(next_state, dtype=torch.float32)
            total_reward += reward
        rewards.append(total_reward)
    return sum(rewards) / len(rewards)
