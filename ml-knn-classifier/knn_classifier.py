"""
K-Nearest Neighbors (KNN) Classifier - implemented from scratch.

KNN is a simple, non-parametric supervised learning algorithm.
For classification, it predicts the class of a point by finding the
K closest training samples (by Euclidean distance) and returning the
majority class label among those neighbours.

Time Complexity:
  - fit:     O(1)  — just stores the training data
  - predict: O(n * m) per query point, where n = training samples,
             m = number of features

Space Complexity: O(n * m)
"""

from collections import Counter
from typing import List


class KNNClassifier:
    def __init__(self, k: int = 3):
        """
        Parameters
        ----------
        k : int
            Number of nearest neighbours to consider (default 3).
        """
        if k < 1:
            raise ValueError("k must be a positive integer")
        self.k = k
        self._X_train: List[List[float]] = []
        self._y_train: List[int] = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def fit(self, X: List[List[float]], y: List[int]) -> "KNNClassifier":
        """Store training data.

        Parameters
        ----------
        X : 2-D list of shape (n_samples, n_features)
        y : 1-D list of length n_samples — class labels (integers)

        Returns
        -------
        self
        """
        if len(X) != len(y):
            raise ValueError("X and y must have the same number of samples")
        self._X_train = X
        self._y_train = y
        return self

    def predict(self, X: List[List[float]]) -> List[int]:
        """Predict class labels for each row in X.

        Parameters
        ----------
        X : 2-D list of shape (n_queries, n_features)

        Returns
        -------
        List[int] — predicted class label for every query point
        """
        return [self._predict_single(x) for x in X]

    def score(self, X: List[List[float]], y: List[int]) -> float:
        """Return accuracy on (X, y).

        Parameters
        ----------
        X : 2-D list of shape (n_samples, n_features)
        y : ground-truth labels

        Returns
        -------
        float in [0.0, 1.0]
        """
        predictions = self.predict(X)
        correct = sum(p == t for p, t in zip(predictions, y))
        return correct / len(y)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _euclidean_distance(
        self, a: List[float], b: List[float]
    ) -> float:
        """Return the Euclidean distance between vectors a and b."""
        return sum((ai - bi) ** 2 for ai, bi in zip(a, b)) ** 0.5

    def _predict_single(self, x: List[float]) -> int:
        """Return the majority label among the k nearest training points."""
        distances = [
            (self._euclidean_distance(x, x_train), label)
            for x_train, label in zip(self._X_train, self._y_train)
        ]
        distances.sort(key=lambda t: t[0])
        k_nearest_labels = [label for _, label in distances[:self.k]]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


# ---------------------------------------------------------------------------
# Quick smoke-test / usage example
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Simple 2-D dataset: two linearly separable classes
    X_train = [
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
    ]
    y_train = [0, 0, 1, 1, 0, 1]

    X_test = [[1.2, 1.9], [6.0, 9.0]]
    y_test = [0, 1]

    clf = KNNClassifier(k=3)
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)
    accuracy = clf.score(X_test, y_test)

    print("Predictions:", predictions)   # Expected: [0, 1]
    print(f"Accuracy:    {accuracy:.2f}")  # Expected: 1.00
