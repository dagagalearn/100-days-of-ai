import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

sns.pairplot(
    data=iris,
    hue='species',
    diag_kind='kde',
    palette='Set2',
    markers=['o', 's', 'D']
)
plt.suptitle("Iris Pairplot", y=1.02)
plt.show()

corr = iris.corr()
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=0.5,
    square=True
)
plt.title("Iris Feature Correlation Heatmap")
plt.show()
