def findCheapestPrice(n, flights, src, dst, K):
    """
    Finds the cheapest price from src to dst with up to K stops.
    
    :param n: Number of nodes (cities).
    :param flights: List of flights represented as (source, destination, price).
    :param src: Source node.
    :param dst: Destination node.
    :param K: Maximum number of stops.
    :return: The cheapest price to get from src to dst with up to K stops. Returns -1 if not possible.
    """
    # Initialize distances with infinity
    distances = [[float('inf')] * n for _ in range(K + 2)]
    distances[0][src] = 0  # Distance to source from source is 0
    
    # Relax the edges K + 1 times to account for up to K stops
    for i in range(1, K + 2):
        distances[i][src] = 0  # Keep source at 0
        for u, v, w in flights:
            # If a cheaper price is found, update the distance
            distances[i][v] = min(distances[i][v], distances[i-1][u] + w)
    
    # The cheapest price after considering up to K stops
    cheapest_price = distances[K + 1][dst]
    return cheapest_price if cheapest_price != float('inf') else -1

# Example usage
if __name__ == "__main__":
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    K = 1
    
    result = findCheapestPrice(n, flights, src, dst, K)
    print(f"The cheapest price from {src} to {dst} with up to {K} stop(s) is: {result}")
