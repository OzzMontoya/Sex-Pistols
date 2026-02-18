def calculate_reward(waiting_time: float, queue_length: float) -> float:
    return -(waiting_time + queue_length)
