from itertools import permutations

def tsp_brute_force(cost):
    n = len(cost)
    cities = list(range(1, n))  # kota selain kota awal (0)

    best_cost = float('inf')
    best_route = None

    # Coba semua permutasi kota (kecuali kota 0 sebagai titik awal)
    for perm in permutations(cities):
        route = [0] + list(perm) + [0]  # mulai dan kembali ke kota 0
        total = 0

        for i in range(len(route) - 1):
            total += cost[route[i]][route[i+1]]

        if total < best_cost:
            best_cost = total
            best_route = route

    return best_route, best_cost

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_route, min_cost = tsp_brute_force(cost_matrix)
print("Best Route:", best_route)
print("Minimum Cost:", min_cost)