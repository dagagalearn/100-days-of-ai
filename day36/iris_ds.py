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


