import csv
import random
import math

# Load the iris dataset from the iris.csv file
with open('iris.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the first row (column names)
    iris_data = [row for row in reader]

# Split the data into a training set and a test set using a 90/10 split
random.shuffle(iris_data)
split_index = math.floor(len(iris_data) * 0.9)
train_data = iris_data[:split_index]
test_data = iris_data[split_index:]

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)-1):
        distance += (float(point1[i]) - float(point2[i])) ** 2
    return math.sqrt(distance)

# Define a function to get the k nearest neighbors of a test point in the training set
def get_nearest_neighbors(train_data, test_point, k):
    distances = []
    for train_point in train_data:
        distance = euclidean_distance(train_point, test_point)
        distances.append((train_point, distance))
    distances.sort(key=lambda x: x[1])
    neighbors = [x[0] for x in distances[:k]]
    return neighbors

# Define a function to predict the class of a test point based on its k nearest neighbors
def predict_class(train_data, test_point, k):
    neighbors = get_nearest_neighbors(train_data, test_point, k)
    class_votes = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        if label in class_votes:
            class_votes[label] += 1
        else:
            class_votes[label] = 1
    sorted_votes = sorted(class_votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_votes[0][0]

# Use the training set to make predictions on the test set and evaluate the accuracy of the classifier
correct_predictions = 0
for test_point in test_data:
    predicted_class = predict_class(train_data, test_point, 1)
    if predicted_class == test_point[-1]:
        correct_predictions += 1

accuracy = correct_predictions / len(test_data)
print("Accuracy:", accuracy)