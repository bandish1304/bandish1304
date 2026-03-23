"""
Linear Regression from scratch using gradient descent.

Predicts a continuous output value given one or more input features.
The model learns weights (coefficients) and a bias (intercept) by
minimising the mean-squared error (MSE) over the training set.
"""

from typing import List, Tuple


class LinearRegression:
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights: List[float] = []
        self.bias: float = 0.0

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def fit(self, X: List[List[float]], y: List[float]) -> None:
        """Fit the model to training data X (n_samples x n_features) and labels y."""
        n_samples = len(X)
        n_features = len(X[0])

        # Initialise weights to zero
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.n_iterations):
            # Forward pass: compute predictions
            predictions = self._predict_raw(X)

            # Compute gradients
            dw = [0.0] * n_features
            db = 0.0
            for i in range(n_samples):
                error = predictions[i] - y[i]
                for j in range(n_features):
                    dw[j] += (2 / n_samples) * error * X[i][j]
                db += (2 / n_samples) * error

            # Update parameters
            self.weights = [self.weights[j] - self.learning_rate * dw[j] for j in range(n_features)]
            self.bias -= self.learning_rate * db

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def predict(self, X: List[List[float]]) -> List[float]:
        """Return predicted values for input X."""
        return self._predict_raw(X)

    def _predict_raw(self, X: List[List[float]]) -> List[float]:
        predictions = []
        for sample in X:
            value = self.bias + sum(self.weights[j] * sample[j] for j in range(len(sample)))
            predictions.append(value)
        return predictions

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def mse(self, X: List[List[float]], y: List[float]) -> float:
        """Mean Squared Error on dataset (X, y)."""
        predictions = self.predict(X)
        n = len(y)
        return sum((predictions[i] - y[i]) ** 2 for i in range(n)) / n

    def r2_score(self, X: List[List[float]], y: List[float]) -> float:
        """Coefficient of determination R² on dataset (X, y)."""
        predictions = self.predict(X)
        y_mean = sum(y) / len(y)
        ss_res = sum((yi - pred) ** 2 for yi, pred in zip(y, predictions))
        ss_tot = sum((yi - y_mean) ** 2 for yi in y)
        if ss_tot == 0:
            return 1.0
        return 1 - ss_res / ss_tot


# ------------------------------------------------------------------
# Quick demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    # y = 2*x + 1  (with slight noise)
    X_train = [[1.0], [2.0], [3.0], [4.0], [5.0]]
    y_train = [3.1, 5.0, 6.9, 9.1, 11.0]

    model = LinearRegression(learning_rate=0.01, n_iterations=2000)
    model.fit(X_train, y_train)

    print(f"Learned weight : {model.weights[0]:.4f}  (expected ≈ 2.0)")
    print(f"Learned bias   : {model.bias:.4f}         (expected ≈ 1.0)")
    print(f"MSE            : {model.mse(X_train, y_train):.6f}")
    print(f"R² score       : {model.r2_score(X_train, y_train):.6f}")

    X_test = [[6.0], [7.0]]
    preds = model.predict(X_test)
    print(f"Predictions for x=6,7: {[round(p, 2) for p in preds]}")
