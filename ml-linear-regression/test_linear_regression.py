"""
Unit tests for the Linear Regression implementation.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from linear_regression import LinearRegression


def test_perfect_linear_fit_1d():
    # y = 3x + 2
    X_train = [[1.0], [2.0], [3.0], [4.0], [5.0]]
    y_train = [5.0, 8.0, 11.0, 14.0, 17.0]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X_train, y_train)
    preds = model.predict([[6.0], [7.0]])
    assert abs(preds[0] - 20.0) < 0.5, f"Expected ~20, got {preds[0]}"
    assert abs(preds[1] - 23.0) < 0.5, f"Expected ~23, got {preds[1]}"
    print("PASS test_perfect_linear_fit_1d")


def test_r2_score_near_one():
    X_train = [[i * 1.0] for i in range(10)]
    y_train = [2.0 * i + 1.0 for i in range(10)]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X_train, y_train)
    r2 = model.score(X_train, y_train)
    assert r2 > 0.99, f"Expected R²>0.99, got {r2}"
    print("PASS test_r2_score_near_one")


def test_multidimensional():
    # y = 2*x1 + 3*x2 + 1
    X_train = [[1, 1], [2, 1], [3, 2], [4, 3]]
    y_train = [6.0, 8.0, 14.0, 18.0]
    model = LinearRegression(learning_rate=0.01, n_iterations=3000)
    model.fit(X_train, y_train)
    r2 = model.score(X_train, y_train)
    assert r2 > 0.99, f"Expected R²>0.99, got {r2}"
    print("PASS test_multidimensional")


def test_predict_returns_list():
    model = LinearRegression()
    model.fit([[1.0], [2.0]], [2.0, 4.0])
    result = model.predict([[3.0]])
    assert isinstance(result, list), "predict should return a list"
    print("PASS test_predict_returns_list")


def test_invalid_learning_rate():
    try:
        LinearRegression(learning_rate=0.0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("PASS test_invalid_learning_rate")


def test_invalid_n_iterations():
    try:
        LinearRegression(n_iterations=0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("PASS test_invalid_n_iterations")


def test_mismatched_xy():
    model = LinearRegression()
    try:
        model.fit([[1.0]], [1.0, 2.0])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("PASS test_mismatched_xy")


if __name__ == "__main__":
    test_perfect_linear_fit_1d()
    test_r2_score_near_one()
    test_multidimensional()
    test_predict_returns_list()
    test_invalid_learning_rate()
    test_invalid_n_iterations()
    test_mismatched_xy()
    print("\nAll Linear Regression tests passed!")
