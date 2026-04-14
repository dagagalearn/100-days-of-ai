from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()
pca = PCA(n_components=2)
X_pr = pca.fit_transform(iris.data)

print(f"Before PCA it has shape of: {iris.data.shape} After transform: {X_pr.shape}")
# Output:
# Before PCA it has shape of: (150, 4) After transform: (150, 2)

plt.scatter(X_pr[:,0], X_pr[:,1], c=iris.target, cmap="viridis")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PC1 vs. PC2 plot")
plt.show()
