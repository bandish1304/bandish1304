"""
Tests for the KMeans implementation.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from k_means_clustering import KMeans


def test_correct_number_of_clusters():
    """fit() should produce exactly k distinct labels."""
    X = [[i * 1.0, i * 1.0] for i in range(30)]
    model = KMeans(k=3, random_state=0)
    model.fit(X)
    assert len(set(model.labels)) == 3


def test_well_separated_clusters():
    """Three tight, well-separated clusters should be identified correctly."""
    cluster_a = [[0.0 + i * 0.05, 0.0] for i in range(10)]
    cluster_b = [[10.0 + i * 0.05, 0.0] for i in range(10)]
    cluster_c = [[20.0 + i * 0.05, 0.0] for i in range(10)]
    X = cluster_a + cluster_b + cluster_c

    model = KMeans(k=3, n_iterations=200, random_state=7)
    model.fit(X)

    # All points within an original cluster must share the same label
    assert len(set(model.labels[:10])) == 1
    assert len(set(model.labels[10:20])) == 1
    assert len(set(model.labels[20:])) == 1

    # The three clusters must have different labels
    label_a = model.labels[0]
    label_b = model.labels[10]
    label_c = model.labels[20]
    assert label_a != label_b
    assert label_b != label_c
    assert label_a != label_c


def test_inertia_positive():
    """Inertia should be non-negative."""
    X = [[float(i), float(i)] for i in range(20)]
    model = KMeans(k=4, random_state=1)
    model.fit(X)
    assert model.inertia(X) >= 0.0


def test_predict_matches_fit_labels():
    """predict() on the training data should return the same labels as fit()."""
    X = [[float(i % 5), float(i % 5)] for i in range(25)]
    model = KMeans(k=3, random_state=2)
    model.fit(X)
    preds = model.predict(X)
    assert preds == model.labels


def test_single_cluster():
    """k=1 should assign every point to label 0."""
    X = [[float(i), float(i)] for i in range(15)]
    model = KMeans(k=1, random_state=0)
    model.fit(X)
    assert all(label == 0 for label in model.labels)


def test_labels_length():
    """Number of labels must equal number of training samples."""
    X = [[float(i), float(j)] for i in range(5) for j in range(5)]
    model = KMeans(k=3, random_state=3)
    model.fit(X)
    assert len(model.labels) == len(X)


if __name__ == "__main__":
    test_correct_number_of_clusters()
    test_well_separated_clusters()
    test_inertia_positive()
    test_predict_matches_fit_labels()
    test_single_cluster()
    test_labels_length()
    print("All K-Means tests passed.")
