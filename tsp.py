from itertools import permutations

def tsp_brute_force(cost):
    n = len(cost)
    cities = list(range(n))
    min_cost = float('inf')
    best_route = None

    for perm in permutations(cities[1:]):
        route = [0] + list(perm) + [0]
        current_cost = sum(cost[route[i]][route[i+1]] for i in range(n))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = route

    return best_route, min_cost

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_route, min_cost = tsp_brute_force(cost_matrix)
print("Best Route:", best_route)
print("Minimum Cost:", min_cost)