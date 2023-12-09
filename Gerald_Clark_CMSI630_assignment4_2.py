# Gerald Clark CMSI assignment 4_Minimax, Alpha Beta Pruning

class Node: 
    def __init__(self, name, value):
        self.value = value
        self.name = name
        self.left = None
        self.right = None

pruned_nodes = 0
alpha_beta_nodes_expanded = 0

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    global pruned_nodes, alpha_beta_nodes_expanded # count both pruned and total expanded nodes

    if depth == 0 or node is None:
        alpha_beta_nodes_expanded += 1
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in [node.left, node.right]:
            alpha_beta_nodes_expanded += 1
            print(f"Expanding {child.name}, Value: {child.value}, Alpha: {alpha}, Beta: {beta}")
            value = max(value, alpha_beta_pruning(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned_nodes += 1 
                print(f"Pruning {child.name}, Value: {child.value}, Alpha: {alpha}, Beta: {beta}")
                break
        return value
    else:
        value = float('inf')
        for child in [node.left, node.right]:
            alpha_beta_nodes_expanded += 1
            print(f"Expanding {child.name}, Value: {child.value}, Alpha: {alpha}, Beta: {beta}")
            value = min(value, alpha_beta_pruning(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                pruned_nodes += 1  
                print(f"Pruning {child.name}, Value: {child.value}, Alpha: {alpha}, Beta: {beta}")
                break
        return value

# Minimax
class MaxPlayer:
    def __init__(self, root):
        self.root = root

class MiniMax:
    total_nodes_visited = 0 

    def __init__(self, max_player):
        self.max_player = max_player
        self.root = max_player.root

    def minimax(self, node):
        best_val, best_move = self.max_value(node)
        return best_val, best_move

    def max_value(self, node):
        print(f"Max value: Expanded Node: {node.name}: {node.value}")
        MiniMax.total_nodes_visited += 1  
        if self.is_terminal(node):
            return self.get_utility(node), None

        max_value = float('-inf')
        best_move = None

        successor_states = self.get_successors(node)
        for state in successor_states:
            value, _ = self.min_value(state, parent=node)
            if value > max_value:
                max_value = value
                best_move = state

        print(f"Max value result: {max_value}, current value for Node: {node.name}")
        return max_value, best_move

    def min_value(self, node, parent=None):
        print(f"Min value: Expanded Node: {node.name}: {node.value}")
        MiniMax.total_nodes_visited += 1 
        if self.is_terminal(node):
            return self.get_utility(node), None

        min_value = float('inf')
        best_move = None

        successor_states = self.get_successors(node)
        for state in successor_states:
            value, _ = self.max_value(state)
            if value < min_value:
                min_value = value
                best_move = state

        print(f"Min value result: {min_value}, current value for Node: {node.name if parent else 'None'}")
        return min_value, best_move

    def get_successors(self, node):
        assert node is not None
        return [node.left, node.right] if node else []

    def is_terminal(self, node):
        assert node is not None
        return node.left is None and node.right is None

    def get_utility(self, node):
        assert node is not None
        return node.value

# Depth 0
root = Node('A', value=None)

# Depth 0
root = Node('A', value=None)

# Depth 1
root.left = Node('B', value=None)
root.right = Node('Q', value=None)

# Depth 2
root.left.left = Node('C', value=None)
root.left.right = Node('J', value=None)
root.right.left = Node('R', value=None)
root.right.right = Node('Z', value=None)

# Depth 3
root.left.left.left = Node('D', value=None)
root.left.left.right = Node('G', value=None)
root.left.right.left = Node('K', value=None)
root.left.right.right = Node('N', value=None)
root.right.left.left = Node('S', value=None)
root.right.left.right = Node('V', value=None)
root.right.right.left = Node('Z1', value=None)
root.right.right.right = Node('Z4', value=None)

# Depth 4
root.left.left.left.left = Node('E', value=10)
root.left.left.left.right = Node('F', value=11)
root.left.left.right.left = Node('H', value=9)
root.left.left.right.right = Node('I', value=12)
root.left.right.left.left = Node('L', value=14)
root.left.right.left.right = Node('M', value=15)
root.left.right.right.left = Node('O', value=13)
root.left.right.right.right = Node('P', value=14)
root.right.left.left.left = Node('T', value=15)
root.right.left.left.right = Node('U', value=2)
root.right.left.right.left = Node('W', value=4)
root.right.left.right.right = Node('X', value=1)
root.right.right.left.left = Node('Z2', value=3)
root.right.right.left.right = Node('Z3', value=22)
root.right.right.right.left = Node('Z5', value=24)
root.right.right.right.right = Node('Z6', value=25)

m1 = MaxPlayer(root)
minimax_instance = MiniMax(m1)
best_value, best_move = minimax_instance.minimax(root)

# Minimax Algorithm
print('\n')
print("__Minimax Algorithm Complete__")
print(f"Top Node value: {best_value}")
print(f"Total Number of Nodes expanded: {MiniMax.total_nodes_visited}")
print('\n')

pruned_nodes = 0  
alpha_beta_nodes_expanded = 0  
m2 = alpha_beta_pruning(root, 4, float('-inf'), float('inf'), True)
print('\n__Alpha Beta Pruning Algorithm__')
print(f"Top Node value: {m2}")
print("Total number of nodes expanded:", alpha_beta_nodes_expanded)
print("Total number of pruned nodes:", pruned_nodes)

# Compare
print("\n__Comparison__")
print(f"Total Number of Nodes expanded for Minimax: {MiniMax.total_nodes_visited}")
print("Total number of nodes expanded for Alpha Beta Pruning:", alpha_beta_nodes_expanded)
print(f"Total Number of Nodes pruned for Alpha Beta Pruning: {pruned_nodes}")

my_savings = ((MiniMax.total_nodes_visited - alpha_beta_nodes_expanded)/MiniMax.total_nodes_visited)
print(f"Total savings: {MiniMax.total_nodes_visited - alpha_beta_nodes_expanded} or {my_savings = :.2%} Alpha Beta Pruning savings")

