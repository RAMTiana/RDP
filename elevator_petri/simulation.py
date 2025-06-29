# Contient la fonction simulate(net, steps)
from .elevator_model import build_elevator_net

def simulate(net, steps=1000):
    """
    Exécute `steps` pas de simulation et renvoie :
    - total_steps
    - useless_moves  (déplacements sans service)
    - requests_served
    """
    stats = {"total_steps": 0, "useless_moves": 0, "requests_served": 0}
    for _ in range(steps):
        res = net.step()
        stats["total_steps"] += 1
        if res:
            fired, name = res
            if name.startswith("move") and not fired:
                stats["useless_moves"] += 1
            if name.startswith("call") and fired:
                stats["requests_served"] += 1
    return stats