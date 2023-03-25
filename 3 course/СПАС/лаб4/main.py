import pandas as pd
import numpy as np
from pprint import pprint

def cosine_distance(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return 1 - (dot_product / (norm_a * norm_b))

def k_means(data, k, max_iterations=100):
    centroids = data.sample(k).values

    for _ in range(max_iterations):
        clusters = {i: [] for i in range(k)}
        for point in data.values:
            distances = [cosine_distance(point, centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)

        new_centroids = [np.mean(clusters[i], axis=0) for i in range(k)]

        if np.all([np.allclose(a, b, rtol=1e-5) for a, b in zip(centroids, new_centroids)]):
            break

        centroids = new_centroids

    return clusters


def cluster_purity(cluster_labels, ground_truth_labels):
    label_count = {}
    for label in ground_truth_labels:
        if label in label_count:
            label_count[label] += 1
        else:
            label_count[label] = 1
        majority_count = max(label_count.values())
        purity = majority_count / len(ground_truth_labels)
    return purity, max(label_count, key=label_count.get)

iris_data = pd.read_csv('iris.csv')
data = iris_data.drop(columns=['variety'])
labels = iris_data['variety']


k = 3
clusters = k_means(data, k)


print("Number of instances in each cluster:")
for i, cluster in clusters.items():
    cluster_labels = []
    for j in range(len(labels)):
        point = data.values[j].tolist()
        for c in cluster:
            if np.allclose(point, c):
                cluster_labels.append(labels.iloc[j])
                break
    purity, majority_label = cluster_purity(cluster_labels, labels)
    print(f"Cluster {i + 1}: {len(cluster)} instances, Majority label: {majority_label}, Purity: {purity:.2f}")

species_counts = iris_data['variety'].value_counts().sort_index()
print("\nKnown class distribution:")
for index, count in species_counts.items():
    print(f"{index}: {count} instances")