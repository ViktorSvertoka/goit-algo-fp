import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight_nodes=[]):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[node]["color"] for node in tree.nodes()]
    labels = {node: tree.nodes[node]["label"] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos, labels=labels, node_color=colors, with_labels=True, node_size=2500
    )
    plt.show()


def bfs(root):
    queue = [root]
    order = []
    while queue:
        current = queue.pop(0)
        order.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return order


def dfs(root):
    stack = [root]
    order = []
    while stack:
        current = stack.pop()
        order.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return order


def assign_colors(nodes):
    num_nodes = len(nodes)
    for i, node in enumerate(nodes):
        shade = int(255 * (i / (num_nodes - 1)))
        color = f"#{shade:02x}{shade:02x}{255 - shade:02x}"
        node.color = color


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація BFS
bfs_order = bfs(root)
assign_colors(bfs_order)
draw_tree(root)

# Відновлення кольорів для DFS візуалізації
for node in bfs_order:
    node.color = "skyblue"

# Візуалізація DFS
dfs_order = dfs(root)
assign_colors(dfs_order)
draw_tree(root)
