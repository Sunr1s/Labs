import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from matplotlib.lines import Line2D

mpg_data = pd.read_csv("mpg2.csv")
data = mpg_data[['displ', 'cyl', 'cty', 'hwy']]  # Select relevant columns for clustering
labels = mpg_data['class']

k = 3
kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
mpg_data['cluster'] = kmeans.labels_

# Encode the class labels as integers for the legend
encoder = LabelEncoder()
mpg_data['encoded_class'] = encoder.fit_transform(labels)

# Create a scatter plot matrix with seaborn
scatter_matrix = sns.pairplot(
    mpg_data,
    vars=data.columns,
    hue='encoded_class',
    palette='Set1',
    markers=['o', 's', 'D'],
    plot_kws={'alpha': 0.8},
)

# Add the centroids to each scatter plot in the matrix
for i in range(scatter_matrix.axes.shape[0]):
    for j in range(scatter_matrix.axes.shape[1]):
        if i != j:
            for centroid, color in zip(kmeans.cluster_centers_, plt.rcParams['axes.prop_cycle']):
                scatter_matrix.axes[i, j].scatter(
                    centroid[j], centroid[i], marker='x', c=color['color'], s=200, lw=2, label='Centroid'
                )

# Customize the legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label=labels[0], markerfacecolor='tab:blue', markersize=10),
                   Line2D([0], [0], marker='s', color='w', label=labels[1], markerfacecolor='tab:orange', markersize=10),
                   Line2D([0], [0], marker='D', color='w', label=labels[2], markerfacecolor='tab:green', markersize=10),
                   Line2D([0], [0], marker='x', color='k', label='Centroid', markeredgewidth=2, markersize=10)]

scatter_matrix.fig.legend(handles=legend_elements, title='Class/centroid', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()