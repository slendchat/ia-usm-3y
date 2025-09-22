from game_tree import generate_game_tree, print_tree
from minimax import minimax
from minimax_ab_pruning import minimax_ab_pruning

import copy
import time

def main():
    tree_depth = 12
    children_per_node = 3
    player = "MIN"

    root_minimax = generate_game_tree(tree_depth,children_per_node)
    root_minimax_ab_pruning = copy.deepcopy(root_minimax)
    # print("Initial tree:")
    # print_tree(root_minimax)

    # MiniMax
    start = time.perf_counter()
    best_value_minimax = minimax(root_minimax, tree_depth, player)
    end = time.perf_counter()
    t_minimax = end - start
    print(f"MiniMax best value: {best_value_minimax}, time: {t_minimax:.6f} sec")

    # MiniMax with alpha-beta pruning
    start = time.perf_counter()
    best_value_ab = minimax_ab_pruning(root_minimax_ab_pruning, tree_depth, player)
    end = time.perf_counter()
    t_ab = end - start
    print(f"Alpha-Beta best value: {best_value_ab}, time: {t_ab:.6f} sec")

    if t_minimax > 0:
        speedup = abs((t_minimax - t_ab) / t_minimax * 100)
        print(f"Alpha-Beta is faster by {speedup:.2f}%")
    else:
        print("Timing error: minimax duration is 0")

    print("minimax times called")
    print(minimax.counter)
    print("minimax ab pruning times called")
    print(minimax_ab_pruning.counter)


if __name__ == "__main__":
    main()