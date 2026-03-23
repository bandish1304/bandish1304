"""
Unit tests for the KNN Classifier implementation.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from knn_classifier import KNNClassifier


def test_basic_classification():
    X_train = [
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
    ]
    y_train = [0, 0, 1, 1, 0, 1]
    clf = KNNClassifier(k=3)
    clf.fit(X_train, y_train)
    preds = clf.predict([[1.2, 1.9], [6.0, 9.0]])
    assert preds == [0, 1], f"Expected [0, 1], got {preds}"
    print("PASS test_basic_classification")


def test_score_perfect():
    X_train = [[0.0], [1.0], [2.0], [3.0]]
    y_train = [0, 0, 1, 1]
    clf = KNNClassifier(k=1)
    clf.fit(X_train, y_train)
    acc = clf.score([[0.0], [1.0], [2.0], [3.0]], [0, 0, 1, 1])
    assert acc == 1.0, f"Expected 1.0, got {acc}"
    print("PASS test_score_perfect")


def test_k1_returns_nearest():
    X_train = [[0.0, 0.0], [10.0, 10.0]]
    y_train = [0, 1]
    clf = KNNClassifier(k=1)
    clf.fit(X_train, y_train)
    preds = clf.predict([[0.1, 0.1], [9.9, 9.9]])
    assert preds == [0, 1], f"Expected [0, 1], got {preds}"
    print("PASS test_k1_returns_nearest")


def test_multiclass():
    X_train = [[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]]
    y_train = [0, 1, 2, 0, 1, 2]
    clf = KNNClassifier(k=1)
    clf.fit(X_train, y_train)
    preds = clf.predict([[0.0], [2.0], [5.0]])
    assert preds == [0, 2, 2], f"Expected [0, 2, 2], got {preds}"
    print("PASS test_multiclass")


def test_invalid_k():
    try:
        KNNClassifier(k=0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("PASS test_invalid_k")


def test_mismatched_xy():
    clf = KNNClassifier(k=1)
    try:
        clf.fit([[1.0, 2.0]], [0, 1])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("PASS test_mismatched_xy")


if __name__ == "__main__":
    test_basic_classification()
    test_score_perfect()
    test_k1_returns_nearest()
    test_multiclass()
    test_invalid_k()
    test_mismatched_xy()
    print("\nAll KNN tests passed!")
