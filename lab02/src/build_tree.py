import numpy as np

np.random.seed(1)

shape = (1,pow(3,5))
max_depth = 5
max_children_per_node = 3

# Node class for the game tree
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = []

# Function to build a sample game tree
def build_weighted_tree(current_depth,max_depth,max_children_per_node,current_value=None):
    if current_depth > max_depth:
        return None
    
    node = Node()

    for i in range(max_children_per_node):
        value = values.pop(0) if current_depth == max_depth else None
        child_node = build_weighted_tree(current_depth + 1, max_depth, max_children_per_node, value)

        if child_node:
            node.children.append(child_node)
            print(f"Added child with value {child_node.value} at depth {current_depth + 1}")
    
    return node




values = np.random.randint(1,100, size=shape)[0]
print("Random values: ", values)
root = build_weighted_tree(1, max_depth, max_children_per_node)

