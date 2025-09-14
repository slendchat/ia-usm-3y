import numpy as np

np.random.seed(1)

shape = (1,pow(3,5))

# Node class for the game tree
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = []

# Function to build a sample game tree
def build_tree():
    pass


def main():
    print("MinMax algorithm demonstration")
    values = np.random.randint(1,100, size=shape)[0]
    print("Random values: ", values)

if __name__ == "__main__":
    main()