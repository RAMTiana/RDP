# Point d'entrée du programme : import des modules et exécution
from elevator_petri.elevator_model import build_elevator_net
from elevator_petri.simulation import simulate
from elevator_petri.visualize import draw_petri


def main():
    """
    Point d'entrée du programme :
    - Construit le réseau de Petri pour un ascenseur à 4 étages
    - Lance la simulation stochastique
    - Affiche les résultats et le schéma
    """
    net = build_elevator_net(num_floors=4)
    print("⏳ Lancement de la simulation…")
    stats = simulate(net, steps=2000)
    print("📊 Statistiques :", stats)
    print("📈 Génération du schéma du réseau de Petri")
    draw_petri(net, out_png="elevator_net.png")


if __name__ == "__main__":
    main()