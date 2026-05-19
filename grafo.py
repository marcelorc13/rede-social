import networkx as nx
from pyvis.network import Network


def construir_grafo():
    G = nx.Graph()

    usuarios = [
        "Alice", "Amaury", "Anamalia", "Aristóteles", "André",
        "Abelardo", "Amilton", "Antonio", "Ivan", "Beatriz",
        "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel",
        "Helena", "Igor", "Juliana", "Marcelo", "Laura",
    ]
    G.add_nodes_from(usuarios)

    amizades = [
        ("Alice", "Amaury"),
        ("Alice", "Anamalia"),
        ("Alice", "Aristóteles"),
        ("Alice", "Beatriz"),
        ("Amaury", "André"),
        ("Amaury", "Abelardo"),
        ("Amaury", "Carlos"),
        ("Anamalia", "Abelardo"),
        ("Anamalia", "Amilton"),
        ("Anamalia", "Diana"),
        ("Aristóteles", "Antonio"),
        ("Aristóteles", "Eduardo"),
        ("André", "Ivan"),
        ("André", "Fernanda"),
        ("Abelardo", "Ivan"),
        ("Abelardo", "Gabriel"),
        ("Amilton", "Antonio"),
        ("Amilton", "Helena"),
        ("Antonio", "Igor"),
        ("Ivan", "Juliana"),
        ("Beatriz", "Carlos"),
        ("Beatriz", "Laura"),
        ("Carlos", "Diana"),
        ("Diana", "Eduardo"),
        ("Eduardo", "Fernanda"),
        ("Fernanda", "Gabriel"),
        ("Gabriel", "Helena"),
        ("Helena", "Igor"),
        ("Igor", "Juliana"),
        ("Juliana", "Marcelo"),
        ("Marcelo", "Laura"),
        ("Marcelo", "Alice"),
        ("Laura", "Anamalia"),
    ]
    G.add_edges_from(amizades)

    return G


def obter_amigos(G, usuario):
    if usuario not in G:
        raise ValueError(f"Usuário '{usuario}' não encontrado no grafo.")
    return list(G.neighbors(usuario))


def grau_separacao(G, u1, u2):
    if u1 not in G:
        raise ValueError(f"Usuário '{u1}' não encontrado no grafo.")
    if u2 not in G:
        raise ValueError(f"Usuário '{u2}' não encontrado no grafo.")
    if not nx.has_path(G, u1, u2):
        return None, None
    grau = nx.shortest_path_length(G, u1, u2)
    caminho = nx.shortest_path(G, u1, u2)
    return grau, caminho


def recomendar_amigos(G, usuario):
    if usuario not in G:
        raise ValueError(f"Usuário '{usuario}' não encontrado no grafo.")
    amigos_diretos = set(G.neighbors(usuario))
    recomendacoes = set()
    for amigo in amigos_diretos:
        for amigo_do_amigo in G.neighbors(amigo):
            if amigo_do_amigo != usuario and amigo_do_amigo not in amigos_diretos:
                recomendacoes.add(amigo_do_amigo)
    return sorted(recomendacoes)


def visualizar(G, saida="grafo.html"):
    rede = Network(height="600px", width="100%", bgcolor="#1a1a2e", font_color="white")
    rede.from_nx(G)
    for no in rede.nodes:
        no["size"] = 20
        no["color"] = "#e94560"
        no["font"] = {"size": 16, "color": "white"}
    for aresta in rede.edges:
        aresta["color"] = "#4a90d9"
    rede.set_options("""
    var options = {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "springLength": 100
        },
        "solver": "forceAtlas2Based"
      }
    }
    """)
    rede.show(saida, notebook=False)
