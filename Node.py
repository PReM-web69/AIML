class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval

root = Node(None, [
    Node(None, [Node(3), Node(5), Node(6)]),
    Node(None, [Node(7), Node(4), Node(5)]),
    Node(None, [Node(6), Node(9), Node(1)])
])

alpha = float('-inf')
beta = float('inf')
depth = 3 
result = alpha_beta_pruning(root, depth, alpha, beta, True)

print(f"Optimal value: {result}")
