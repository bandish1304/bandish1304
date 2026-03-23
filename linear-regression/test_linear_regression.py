"""
Tests for the LinearRegression implementation.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from linear_regression import LinearRegression


def test_perfect_fit():
    """Model should learn y = 3x + 2 almost exactly."""
    X = [[1.0], [2.0], [3.0], [4.0], [5.0]]
    y = [5.0, 8.0, 11.0, 14.0, 17.0]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X, y)
    assert abs(model.weights[0] - 3.0) < 0.1, f"weight={model.weights[0]}"
    assert abs(model.bias - 2.0) < 0.1, f"bias={model.bias}"


def test_r2_high_for_linear_data():
    """R² should be close to 1 for near-linear data."""
    X = [[i * 1.0] for i in range(1, 11)]
    y = [2.0 * i + 1.0 for i in range(1, 11)]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X, y)
    score = model.r2_score(X, y)
    assert score > 0.99, f"R²={score}"


def test_mse_decreases_with_iterations():
    """More iterations should yield a lower MSE."""
    X = [[i * 1.0] for i in range(1, 6)]
    y = [3.0 * i + 0.5 for i in range(1, 6)]

    model_few = LinearRegression(learning_rate=0.01, n_iterations=10)
    model_few.fit(X, y)

    model_many = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model_many.fit(X, y)

    assert model_many.mse(X, y) < model_few.mse(X, y)


def test_prediction_shape():
    """predict() should return the same number of values as input rows."""
    X_train = [[1.0], [2.0], [3.0]]
    y_train = [2.0, 4.0, 6.0]
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict([[4.0], [5.0], [6.0], [7.0]])
    assert len(preds) == 4


def test_multi_feature():
    """Model should fit y = x1 + 2*x2 reasonably well."""
    X = [[1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [4.0, 3.0], [5.0, 2.0]]
    y = [3.0, 6.0, 5.0, 10.0, 9.0]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X, y)
    score = model.r2_score(X, y)
    assert score > 0.95, f"R²={score}"


if __name__ == "__main__":
    test_perfect_fit()
    test_r2_high_for_linear_data()
    test_mse_decreases_with_iterations()
    test_prediction_shape()
    test_multi_feature()
    print("All linear regression tests passed.")
