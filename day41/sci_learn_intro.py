from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)
print(iris.target_names)

print(iris.data.shape)

print(iris.data[:5])
print(iris.target[:5])

for i, name in enumerate(iris.target_names):
    print(i, name)

sample = iris.data[0]
print(sample)
print(iris.target_names[iris.target[0]])
