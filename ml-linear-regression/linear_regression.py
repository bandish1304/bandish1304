"""
Linear Regression — implemented from scratch using Gradient Descent.

Linear Regression models the relationship between a scalar target y and one
or more input features X as a linear function:

    ŷ = X · w + b

The model parameters (weights w and bias b) are learned by minimising the
Mean Squared Error (MSE) loss with Gradient Descent:

    L = (1 / n) * Σ (ŷᵢ − yᵢ)²

    ∂L/∂w = (2 / n) * Xᵀ · (ŷ − y)
    ∂L/∂b = (2 / n) * Σ (ŷᵢ − yᵢ)

Time Complexity (per fit call):
  O(n_iterations * n_samples * n_features)

Space Complexity: O(n_features)
"""

from typing import List


class LinearRegression:
    def __init__(
        self,
        learning_rate: float = 0.01,
        n_iterations: int = 1000,
    ):
        """
        Parameters
        ----------
        learning_rate : float
            Step size for gradient descent (default 0.01).
        n_iterations : int
            Number of gradient-descent steps (default 1 000).
        """
        if learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if n_iterations < 1:
            raise ValueError("n_iterations must be at least 1")

        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self._weights: List[float] = []
        self._bias: float = 0.0

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def fit(
        self, X: List[List[float]], y: List[float]
    ) -> "LinearRegression":
        """Learn weights and bias via gradient descent.

        Parameters
        ----------
        X : 2-D list of shape (n_samples, n_features)
        y : 1-D list of length n_samples — target values

        Returns
        -------
        self
        """
        if len(X) != len(y):
            raise ValueError("X and y must have the same number of samples")

        n_samples = len(X)
        n_features = len(X[0]) if n_samples > 0 else 0

        # Initialise parameters to zero
        self._weights = [0.0] * n_features
        self._bias = 0.0

        for _ in range(self.n_iterations):
            # Forward pass: ŷ = X·w + b
            y_pred = self._linear(X)

            # Residuals: (ŷ - y)
            residuals = [y_pred[i] - y[i] for i in range(n_samples)]

            # Gradients
            dw = [
                (2.0 / n_samples)
                * sum(residuals[i] * X[i][j] for i in range(n_samples))
                for j in range(n_features)
            ]
            db = (2.0 / n_samples) * sum(residuals)

            # Parameter update
            self._weights = [
                self._weights[j] - self.learning_rate * dw[j]
                for j in range(n_features)
            ]
            self._bias -= self.learning_rate * db

        return self

    def predict(self, X: List[List[float]]) -> List[float]:
        """Predict continuous target values for each row in X.

        Parameters
        ----------
        X : 2-D list of shape (n_queries, n_features)

        Returns
        -------
        List[float] — predicted value for every query point
        """
        return self._linear(X)

    def score(self, X: List[List[float]], y: List[float]) -> float:
        """Return the coefficient of determination R².

        R² = 1 − SS_res / SS_tot
            where SS_res = Σ(yᵢ − ŷᵢ)²
                  SS_tot = Σ(yᵢ − ȳ)²

        Parameters
        ----------
        X : 2-D list of shape (n_samples, n_features)
        y : ground-truth target values

        Returns
        -------
        float — R² score (1.0 = perfect prediction)
        """
        y_pred = self.predict(X)
        y_mean = sum(y) / len(y)

        ss_res = sum((yi - ypi) ** 2 for yi, ypi in zip(y, y_pred))
        ss_tot = sum((yi - y_mean) ** 2 for yi in y)

        if ss_tot == 0:
            return 1.0 if ss_res == 0 else 0.0

        return 1.0 - ss_res / ss_tot

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _linear(self, X: List[List[float]]) -> List[float]:
        """Compute ŷ = X · w + b for every row in X."""
        result = []
        for row in X:
            pred = sum(row[j] * self._weights[j] for j in range(len(row)))
            result.append(pred + self._bias)
        return result


# ---------------------------------------------------------------------------
# Quick smoke-test / usage example
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # y = 2*x1 + 3*x2 + 1  (with a little noise)
    X_train = [
        [1.0, 1.0], [2.0, 1.0], [3.0, 2.0],
        [4.0, 3.0], [5.0, 3.0], [6.0, 4.0],
    ]
    y_train = [6.0, 8.0, 14.0, 18.0, 20.0, 25.0]

    model = LinearRegression(learning_rate=0.01, n_iterations=2000)
    model.fit(X_train, y_train)

    X_test = [[7.0, 5.0], [2.0, 2.0]]
    y_test = [30.0, 11.0]

    predictions = model.predict(X_test)
    r2 = model.score(X_test, y_test)

    print("Predictions:", [round(p, 2) for p in predictions])
    print(f"R² score:    {r2:.4f}")   # Expected: close to 1.0
    print(f"Weights:     {[round(w, 2) for w in model._weights]}")
    print(f"Bias:        {model._bias:.2f}")
