<h2>Linear Regression (Gradient Descent)</h2>
<h3>AI / Machine Learning — Regression</h3>
<hr>

<h3>Description</h3>
<p>
  Implement <strong>Linear Regression</strong> from scratch using
  <strong>Gradient Descent</strong> (without using any external ML libraries).
</p>
<p>
  The model learns a linear mapping from input features to a continuous target:
</p>
<pre>ŷ = X · w + b</pre>
<p>
  Parameters <em>w</em> (weights) and <em>b</em> (bias) are updated iteratively
  to minimise the <strong>Mean Squared Error (MSE)</strong>:
</p>
<pre>
L  = (1/n) · Σ (ŷᵢ − yᵢ)²
∂L/∂w = (2/n) · Xᵀ · (ŷ − y)
∂L/∂b = (2/n) · Σ (ŷᵢ − yᵢ)
</pre>

<h3>Interface to Implement</h3>
<pre>
class LinearRegression:
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000): ...
    def fit(self, X: List[List[float]], y: List[float]) -&gt; "LinearRegression": ...
    def predict(self, X: List[List[float]]) -&gt; List[float]: ...
    def score(self, X: List[List[float]], y: List[float]) -&gt; float: ...
</pre>

<h3>Example</h3>
<pre>
# Underlying relationship: y ≈ 2·x₁ + 3·x₂ + 1
X_train = [[1,1],[2,1],[3,2],[4,3],[5,3],[6,4]]
y_train  = [6, 8, 14, 18, 20, 25]

model = LinearRegression(learning_rate=0.01, n_iterations=2000)
model.fit(X_train, y_train)

model.predict([[7, 5]])   # ≈ [30.0]
model.score([[7, 5]], [30.0])  # ≈ 1.0
</pre>

<h3>Constraints</h3>
<ul>
  <li><code>learning_rate &gt; 0</code></li>
  <li><code>n_iterations &gt;= 1</code></li>
  <li>All feature and target values are real numbers.</li>
  <li>Number of features is the same for train and test data.</li>
</ul>

<h3>Complexity</h3>
<ul>
  <li><strong>fit:</strong> O(n_iterations · n_samples · n_features)</li>
  <li><strong>predict:</strong> O(n_queries · n_features)</li>
  <li><strong>Space:</strong> O(n_features)</li>
</ul>
