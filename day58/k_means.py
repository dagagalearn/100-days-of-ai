import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/codebasics/py/master/ML/13_kmeans/income.csv"

df = pd.read_csv(url)
df = df[["Age","Income($)"]]

km = KMeans(n_clusters=3)
y_pred = km.fit_predict(df)
df["cluster"] = y_pred
df0 = df[df.cluster==0]
df1 = df[df.cluster==1]
df2 = df[df.cluster==2]

plt.scatter(df1.Age, df1["Income($)"],color="green")
plt.scatter(df0.Age, df0["Income($)"],color="red")
plt.scatter(df2.Age, df2["Income($)"],color="black")
plt.show()

sse = []  
k_range = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df)
    sse.append(km.inertia_)

plt.plot(k_range, sse, marker='o')
plt.xlabel("Number of clusters (K)")
plt.ylabel("SSE (Inertia)")
plt.title("Elbow Method for Optimal K")
plt.show()
