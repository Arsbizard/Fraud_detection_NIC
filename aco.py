import numpy as np


# generic ACO algorithm for TSP
class AntColony:
    def __init__(self, distances, n_ants, n_iterations, decay, alpha=1, beta=1):
        self.distances = distances
        self.pheromones = np.ones(distances.shape) / len(distances)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        shortest_distance = float('inf')
        for i in range(self.n_iterations):
            paths = self._construct_solutions()
            distances = [self._path_distance(path) for path in paths]
            self._update_pheromones(paths, distances)
            # Update pheromones based on paths and distances

            best_idx = np.argmin(distances)
            if distances[best_idx] < shortest_distance:
                shortest_distance = distances[best_idx]
                shortest_path = paths[best_idx]
            self.pheromones *= self.decay
        return shortest_path, shortest_distance

    def _construct_solutions(self):
        paths = []

        for ant in range(self.n_ants):
            path = self._construct_path()
            paths.append(path)

        return paths

    def _construct_path(self):
        path = [0]  # Start from node 0
        remaining = set(range(1, self.distances.shape[0]))
        while remaining:
            next_node = self._select_next(path[-1], remaining)
            path.append(next_node)

            remaining.remove(next_node)

        return path

    def _select_next(self, current, remaining):
        choices = list(remaining)
        probs = [self.pheromones[current][j] ** self.alpha * self._distance_heuristic(current, j) ** self.beta for j in
                 choices]
        probs /= np.sum(probs)

        return np.random.choice(choices, p=probs)

    def _distance_heuristic(self, i, j):
        return 1 / self.distances[i][j]

    def _path_distance(self, path):
        return sum([self.distances[path[i]][path[i + 1]] for i in range(len(path) - 1)])

    def _update_pheromones(self, paths, distances):
        for i in range(self.distances.shape[0]):
            for j in range(self.distances.shape[1]):
                for path, distance in zip(paths, distances):
                    index_of_i = np.where(np.array(path) == i)[0]
                    # Check if node j follows node i in the path and update pheromones (For both directions)
                    if index_of_i.size > 0:
                        index_of_i = index_of_i[0]

                    if index_of_i + 1 < len(path) and path[index_of_i + 1] == j:
                        self.pheromones[i][j] += 1 / distance
                        self.pheromones[j][i] += 1 / distance
