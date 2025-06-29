from graphviz import Digraph
import matplotlib.pyplot as plt

def draw_petri(net, out_png="net.png"):
    """Génère le schéma Graphviz et le sauvegarde en image PNG."""
    # Création du graphe
    dot = Digraph(format='png')

    # Ajout des places
    for p in net.places.values():
        # Construction du label avec concaténation sûre
        label = p.name + "\nTokens=" + str(p.tokens)
        dot.node(p.name, shape='circle', label=label)

    # Ajout des transitions et des arcs
    for t in net.transitions.values():
        dot.node(t.name, shape='box', label=t.name)
        for inp in t.input_places:
            dot.edge(inp.name, t.name)
        for out in t.output_places:
            dot.edge(t.name, out.name)

    # Génération du fichier PNG
    dot.render(filename=out_png.replace('.png',''), cleanup=True)

    # Lecture et sauvegarde de l'image sans affichage interactif
    img = plt.imread(out_png)
    plt.imsave(out_png, img)
    plt.close()