# Contient les classes Place, Transition, PetriNet définies plus bas
import random

class Place:
    """Représente une place du réseau avec un compteur de jetons."""
    def __init__(self, name, tokens=0):
        self.name = name
        self.tokens = tokens

class Transition:
    """Représente une transition stochastique avec des arcs d'entrée et de sortie."""
    def __init__(self, name, rate=1.0):
        self.name = name
        self.rate = rate
        self.input_places = []
        self.output_places = []

    def add_input(self, place): self.input_places.append(place)
    def add_output(self, place): self.output_places.append(place)
    def is_enabled(self): return all(p.tokens > 0 for p in self.input_places)

    def fire(self):
        if not self.is_enabled(): return False
        for p in self.input_places: p.tokens -= 1
        for p in self.output_places: p.tokens += 1
        return True

class PetriNet:
    """Gestion globale du réseau : places, transitions et simulation d'un pas."""
    def __init__(self):
        self.places = {}
        self.transitions = {}

    def add_place(self, name, tokens=0): self.places[name] = Place(name, tokens)
    def add_transition(self, name, rate=1.0): self.transitions[name] = Transition(name, rate)

    def add_arc(self, src, dst):
        if src in self.places and dst in self.transitions:
            self.transitions[dst].add_input(self.places[src])
        elif src in self.transitions and dst in self.places:
            self.transitions[src].add_output(self.places[dst])

    def step(self):
        enabled = [t for t in self.transitions.values() if t.is_enabled()]
        if not enabled: return None
        total_rate = sum(t.rate for t in enabled)
        r = random.uniform(0, total_rate)
        cum = 0
        for t in enabled:
            cum += t.rate
            if r <= cum:
                return t.fire(), t.name
        return None