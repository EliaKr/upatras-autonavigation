# Παίρνει είσοδο της μορφής positions = [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
# χρόνος σε ms

def plot(positions, solvingtime, distance_travelled):
    x = []
    y = []
    for i in positions:
        x.append(i[0])
        y.append(i[1])
    
    plt.xlabel(f"Solving Time: {solvingtime}ms, Distance Travelled: {distance_travelled}")
    plt.plot(x, y, "b--", linewidth=8.0)
    
plot(positions, solving_time, dist)