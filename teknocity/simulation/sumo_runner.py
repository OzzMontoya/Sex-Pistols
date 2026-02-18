import traci


def start_simulation(config_path: str):
    traci.start(["sumo", "-c", config_path])
