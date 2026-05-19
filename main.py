import argparse
import webbrowser
import sys
import grafo as g


def cmd_amigos(args):
    G = g.construir_grafo()
    try:
        amigos = g.obter_amigos(G, args.usuario)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
    if amigos:
        print(f"Amigos de {args.usuario}: {', '.join(amigos)}")
    else:
        print(f"{args.usuario} não possui amigos.")


def cmd_separacao(args):
    G = g.construir_grafo()
    try:
        grau, caminho = g.grau_separacao(G, args.usuario1, args.usuario2)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
    if grau is None:
        print(f"Sem caminho entre {args.usuario1} e {args.usuario2}.")
    else:
        print(f"Graus de separação: {grau}")
        print(f"Caminho: {' -> '.join(caminho)}")


def cmd_recomendar(args):
    G = g.construir_grafo()
    try:
        recs = g.recomendar_amigos(G, args.usuario)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
    if recs:
        print(f"Recomendações para {args.usuario}: {', '.join(recs)}")
    else:
        print(f"Sem recomendações para {args.usuario}.")


def cmd_visualizar(args):
    G = g.construir_grafo()
    saida = "grafo.html"
    g.visualizar(G, saida)
    print(f"Grafo salvo em {saida}. Abrindo navegador...")
    webbrowser.open(saida)


def main():
    parser = argparse.ArgumentParser(description="Mini Rede Social - Demonstração de Teoria dos Grafos")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # lista todos os amigos de um usuário
    p_amigos = subparsers.add_parser("amigos", help="Lista os amigos de um usuário")
    p_amigos.add_argument("usuario")
    p_amigos.set_defaults(func=cmd_amigos)

    # calcula grau de separação entre dois usuários
    p_sep = subparsers.add_parser("separacao", help="Grau de separação entre dois usuários (BFS)")
    p_sep.add_argument("usuario1")
    p_sep.add_argument("usuario2")
    p_sep.set_defaults(func=cmd_separacao)

    # recomenda novos amigos para um usuário
    p_rec = subparsers.add_parser("recomendar", help="Recomenda amigos de amigos")
    p_rec.add_argument("usuario")
    p_rec.set_defaults(func=cmd_recomendar)

    # abre grafo.html
    p_vis = subparsers.add_parser("visualizar", help="Gera grafo interativo (grafo.html)")
    p_vis.set_defaults(func=cmd_visualizar)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
