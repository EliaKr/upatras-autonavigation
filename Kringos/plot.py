# Παίρνει είσοδο της μορφής positions = [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
# χρόνος σε ms

def plot(positions, solvingtime_ms = "Unknown", distance_travelled = "Unknown"):
    x = []
    y = []
    for i in positions:
        x.append(i[0])
        y.append(i[1])
    if len(positions) > 1:
        plt.xlabel(f"Solving Time: {solvingtime_ms}ms, Distance Travelled: {distance_travelled}")
    else:
        plt.xlabel(f"Unsolvable")
    
    plt.plot(x, y, "b-", linewidth=8.0)