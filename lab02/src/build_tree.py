import numpy as np

np.random.seed(1)


# Node class for the game tree
class Node:
    def __init__(self, value=None, player=None, children=None):
        self.value = value
        self.player=player
        self.children = []

# Function to build a sample game tree
def build_weighted_tree(current_depth,max_depth,max_children_per_node,values):
    if current_depth > max_depth:
        return None

    value = values.pop(0) if current_depth == max_depth else None
    player = "MAX" if current_depth % 2 == 0 else "MIN"
    node = Node(value,player)

    for i in range(max_children_per_node):

        child_node = build_weighted_tree(current_depth + 1, max_depth, max_children_per_node, values)

        if child_node:
            node.children.append(child_node)

    return node

def print_tree(node, prefix="", is_last=True):
    # печатаем сам узел
    connector = "└── " if is_last else "├── "
    value = node.value if node.value is not None else "None"
    print(prefix + connector + str(value) + " " + str(node.player))

    # подготавливаем отступ для детей
    prefix += "    " if is_last else "│   "

    # печатаем детей
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last_child = (i == (child_count - 1))
        print_tree(child, prefix, is_last_child)

def generate_game_tree(max_depth,max_children_per_node):
    shape = (1,pow(max_children_per_node,max_depth-1))
    values = np.random.randint(1,100, size=shape)[0].tolist()
    # values = list(range(1, shape[1] + 1))
    root = build_weighted_tree(1, max_depth, max_children_per_node,values)
    return root




