# Mini Rede Social — Teoria dos Grafos

Aplicação CLI que modela uma rede social como **grafo não-direcionado** usando NetworkX. Implementa BFS para calcular grau de separação entre usuários e recomenda novas conexões via amigos de amigos. Gera visualização interativa em HTML via Pyvis.

## Modelagem

| Elemento | Representação |
|----------|--------------|
| Vértice  | Usuário da rede |
| Aresta   | Amizade entre dois usuários |
| Tipo     | Grafo não-direcionado e não-ponderado |

## Algoritmos

- **BFS (Busca em Largura):** calcula grau de separação e caminho mais curto entre dois usuários
- **Amigos de amigos:** percorre 2 níveis do grafo, filtra amigos já existentes e retorna recomendações

## Estrutura

```
rede-social/
├── grafo.py   # lógica: grafo, BFS, recomendação, visualização
├── main.py    # CLI: subcomandos via argparse
└── README.md
```

## Instalação

```bash
pip install networkx pyvis
```

## Uso

### Listar amigos de um usuário

```bash
python main.py amigos <usuario>
```

Exemplo:
```bash
python main.py amigos Alice
# Amigos de Alice: Amaury, Anamalia, Aristóteles, Beatriz, Klaus
```

### Grau de separação entre dois usuários (BFS)

```bash
python main.py separacao <usuario1> <usuario2>
```

Exemplo:
```bash
python main.py separacao Alice Igor
# Graus de separação: 3
# Caminho: Alice -> Aristóteles -> Antonio -> Igor
```

### Recomendar amigos de amigos

```bash
python main.py recomendar <usuario>
```

Exemplo:
```bash
python main.py recomendar Alice
# Recomendações para Alice: Abelardo, Amilton, André, Antonio, Carlos, Diana, Eduardo, Juliana, Laura
```

### Visualizar grafo interativo

```bash
python main.py visualizar
```

Gera `grafo.html` e abre no navegador. Nós e arestas são interativos (arrastar, zoom, hover).

## Usuários disponíveis

`Alice`, `Amaury`, `Anamalia`, `Aristóteles`, `André`, `Abelardo`, `Amilton`, `Antonio`, `Ivan`, `Beatriz`, `Carlos`, `Diana`, `Eduardo`, `Fernanda`, `Gabriel`, `Helena`, `Igor`, `Juliana`, `Klaus`, `Laura`
