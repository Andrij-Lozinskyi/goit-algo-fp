import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  
        self.color = "skyblue"  

def add_edges(graph, node, pos, colors, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        colors.append(node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, colors, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, colors, x=r, y=y - 1, layer=layer + 1)

def get_next_color(depth):
    color = "#"+"".join([f"{int((256 - depth*20) % 256):02x}"]*3)
    return color

def dfs(node, depth=0):
    if node:
        node.color = get_next_color(depth)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

def bfs(root):
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node:
            node.color = get_next_color(depth)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    colors = []
    add_edges(tree, tree_root, pos, colors)
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, edge_color="gray")
    plt.show()

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з DFS
dfs(root)
draw_tree(root)

# Скидання кольорів
root.color, root.left.color, root.left.left.color, root.left.right.color, root.right.color, root.right.left.color = ["skyblue"]*6

# Відображення дерева з BFS
bfs(root)
draw_tree(root)
