# Contient la fonction draw_petri(net, out_png)
from graphviz import Digraph
import matplotlib.pyplot as plt

def draw_petri(net, out_png="net.png"):
    """Génère le schéma Graphviz et l'affiche avec matplotlib."""
    dot = Digraph(format='png')
    # Noeuds : places
    for p in net.places.values():
        dot.node(p.name, shape='circle', label=f"{p.name}\nTokens={p.tokens}")
    # Noeuds : transitions et arcs
    for t in net.transitions.values():
        dot.node(t.name, shape='box', label=t.name)
        for inp in t.input_places:
            dot.edge(inp.name, t.name)
        for out in t.output_places:
            dot.edge(t.name, out.name)
    dot.render(out_png.replace('.png',''), cleanup=True)
    img = plt.imread(out_png)
    plt.imshow(img)
    plt.axis('off')
    plt.show()