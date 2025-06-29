# Contient la fonction build_elevator_net(num_floors)
from .petri import PetriNet

def build_elevator_net(num_floors=3):
    """
    Construit un réseau de Petri pour un ascenseur à `num_floors` étages :
    - Places de requête (`req_i`)
    - Places de position (`pos_i`)
    - Transitions d'appel (`call_i`)
    - Transitions de déplacement (`move_i_to_j`)
    """
    net = PetriNet()
    # Création des places
    for i in range(1, num_floors+1):
        net.add_place(f"req_{i}", tokens=0)
        net.add_place(f"pos_{i}", tokens=1 if i == 1 else 0)
    # Transitions d'appel
    for i in range(1, num_floors+1):
        name = f"call_{i}"
        net.add_transition(name, rate=0.1 * i)
        net.add_arc(f"req_{i}", name)
        net.add_arc(name, f"req_{i}")
    # Transitions de déplacement entre étages adjacents
    for src in range(1, num_floors+1):
        for dst in (src-1, src+1):
            if 1 <= dst <= num_floors:
                t = f"move_{src}_to_{dst}"
                net.add_transition(t, rate=1.0)
                net.add_arc(f"pos_{src}", t)
                net.add_arc(t, f"pos_{dst}")
    return net