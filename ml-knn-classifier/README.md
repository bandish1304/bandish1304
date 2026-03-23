<h2>K-Nearest Neighbors (KNN) Classifier</h2>
<h3>AI / Machine Learning — Classification</h3>
<hr>

<h3>Description</h3>
<p>
  Implement a <strong>K-Nearest Neighbors (KNN) Classifier</strong> from scratch
  (without using any external ML libraries such as scikit-learn).
</p>
<p>
  KNN is a non-parametric, lazy-learning algorithm. At prediction time it
  finds the <em>k</em> training points whose feature vectors are closest to the
  query point (using Euclidean distance) and returns the <strong>majority class
  label</strong> among those neighbours.
</p>

<h3>Interface to Implement</h3>
<pre>
class KNNClassifier:
    def __init__(self, k: int = 3): ...
    def fit(self, X: List[List[float]], y: List[int]) -&gt; "KNNClassifier": ...
    def predict(self, X: List[List[float]]) -&gt; List[int]: ...
    def score(self, X: List[List[float]], y: List[int]) -&gt; float: ...
</pre>

<h3>Example</h3>
<pre>
X_train = [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
           [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]
y_train = [0, 0, 1, 1, 0, 1]

clf = KNNClassifier(k=3)
clf.fit(X_train, y_train)

clf.predict([[1.2, 1.9], [6.0, 9.0]])
# Output: [0, 1]

clf.score([[1.2, 1.9], [6.0, 9.0]], [0, 1])
# Output: 1.0
</pre>

<h3>Constraints</h3>
<ul>
  <li><code>1 &lt;= k &lt;= n_training_samples</code></li>
  <li>All feature values are real numbers.</li>
  <li>Class labels are non-negative integers.</li>
  <li>Number of features is the same for train and test data.</li>
</ul>

<h3>Complexity</h3>
<ul>
  <li><strong>fit:</strong> O(1) — stores the training data</li>
  <li><strong>predict:</strong> O(n · m) per query, where n = training samples,
      m = features</li>
  <li><strong>Space:</strong> O(n · m)</li>
</ul>
