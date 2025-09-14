
def minimax(node, current_depth, player_name) -> float:
    if current_depth == 1:
        return node.value

    if player_name == "MAX":
        best_value = float("-inf")
        for child in node.children:
            eval = minimax(child,current_depth - 1, "MIN")
            best_value = max(best_value,eval)
        node.value = best_value
        return best_value
    else:
        best_value = float("inf")
        for child in node.children:
            eval = minimax(child,current_depth -1, "MAX")
            best_value = min(best_value,eval)
        node.value = best_value
        return best_value
