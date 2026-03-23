"""
K-Means Clustering from scratch.

Groups n_samples data points into k clusters by iteratively:
  1. Assigning each point to its nearest centroid (Euclidean distance).
  2. Recomputing each centroid as the mean of its assigned points.

No external libraries are required — only the Python standard library.
"""

import random
from typing import List, Tuple, Optional


class KMeans:
    def __init__(self, k: int, n_iterations: int = 100, random_state: Optional[int] = None):
        self.k = k
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.centroids: List[List[float]] = []
        self.labels: List[int] = []

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def fit(self, X: List[List[float]]) -> None:
        """Fit k centroids to dataset X (n_samples x n_features)."""
        if self.random_state is not None:
            random.seed(self.random_state)

        n_samples = len(X)
        n_features = len(X[0])

        # Initialise centroids by picking k random data points (kmeans++ could
        # be used here, but random init keeps the implementation simple)
        indices = random.sample(range(n_samples), self.k)
        self.centroids = [list(X[i]) for i in indices]

        for _ in range(self.n_iterations):
            # Assign step
            new_labels = [self._nearest_centroid(point) for point in X]

            # Update step
            new_centroids = self._compute_centroids(X, new_labels, n_features)

            # Check for convergence
            if new_centroids == self.centroids:
                self.labels = new_labels
                break

            self.centroids = new_centroids
            self.labels = new_labels

    def predict(self, X: List[List[float]]) -> List[int]:
        """Assign each row of X to the nearest centroid."""
        return [self._nearest_centroid(point) for point in X]

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def inertia(self, X: List[List[float]]) -> float:
        """Sum of squared distances from each point to its assigned centroid."""
        total = 0.0
        labels = self.predict(X)
        for i, point in enumerate(X):
            total += self._squared_distance(point, self.centroids[labels[i]])
        return total

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _nearest_centroid(self, point: List[float]) -> int:
        distances = [self._squared_distance(point, c) for c in self.centroids]
        return distances.index(min(distances))

    @staticmethod
    def _squared_distance(a: List[float], b: List[float]) -> float:
        return sum((a[i] - b[i]) ** 2 for i in range(len(a)))

    def _compute_centroids(
        self, X: List[List[float]], labels: List[int], n_features: int
    ) -> List[List[float]]:
        new_centroids = []
        for cluster_id in range(self.k):
            members = [X[i] for i in range(len(X)) if labels[i] == cluster_id]
            if members:
                centroid = [
                    sum(m[f] for m in members) / len(members) for f in range(n_features)
                ]
            else:
                # Keep old centroid if cluster is empty
                centroid = list(self.centroids[cluster_id])
            new_centroids.append(centroid)
        return new_centroids


# ------------------------------------------------------------------
# Quick demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    # Three well-separated 2-D clusters
    cluster_a = [[1.0 + i * 0.1, 1.0 + i * 0.1] for i in range(10)]
    cluster_b = [[5.0 + i * 0.1, 5.0 + i * 0.1] for i in range(10)]
    cluster_c = [[9.0 + i * 0.1, 1.0 + i * 0.1] for i in range(10)]
    X = cluster_a + cluster_b + cluster_c

    model = KMeans(k=3, n_iterations=100, random_state=42)
    model.fit(X)

    print("Centroids:")
    for idx, c in enumerate(model.centroids):
        print(f"  Cluster {idx}: ({c[0]:.2f}, {c[1]:.2f})")

    print(f"Inertia: {model.inertia(X):.4f}")

    # All points from the same source cluster should share a label
    labels_a = set(model.labels[:10])
    labels_b = set(model.labels[10:20])
    labels_c = set(model.labels[20:])
    print(f"Labels per original cluster: A={labels_a}  B={labels_b}  C={labels_c}")
    assert len(labels_a) == 1 and len(labels_b) == 1 and len(labels_c) == 1
    assert labels_a != labels_b and labels_b != labels_c and labels_a != labels_c
    print("Demo passed: each original cluster maps to a unique label.")
