def minimax_ab_pruning(node, current_depth, player_name, alpha=float("-inf"), beta=float("inf")) -> float:
    if not hasattr(minimax_ab_pruning, "counter"):
        minimax_ab_pruning.counter = 0
    minimax_ab_pruning.counter += 1

    if current_depth == 1:
        return node.value
    
    if player_name == "MAX":
        best_value = float("-inf")
        for child in node.children:
            eval = minimax_ab_pruning(child,current_depth - 1, "MIN", alpha, beta)
            best_value = max(best_value,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        node.value = best_value
        return best_value
    else:
        best_value = float("inf")
        for child in node.children:
            eval = minimax_ab_pruning(child,current_depth -1, "MAX", alpha, beta)
            best_value = min(best_value,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        node.value = best_value
        return best_value