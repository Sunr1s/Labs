import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.metrics import classification_report

# Load the data from the file "Vehicle.csv" into a pandas dataframe
df = pd.read_csv("Vehicle.csv")

# Divide the data into features (X) and target (y)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Split the data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Scale the features using normalization
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVM classifier on the training data
clf = svm.SVC(kernel='linear', C=1, random_state=0)
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the classifier's performance
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Build the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the performance of the classifier
print(classification_report(y_test, y_pred))
 
# Select two features from the data
X = df[['Comp', 'Circ']].values
y = df['Class'].values

# Encode the class labels as numbers
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the SVM classifier on the training data
clf = svm.SVC(kernel='linear', C=1, random_state=0)
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')

# Plot the decision boundary of the classifier
w = clf.coef_[0]
b = clf.intercept_[0]
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2), np.arange(y_min, y_max, 0.2))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, colors='k')

plt.xlabel('Comp')
plt.ylabel('Circ')
plt.title('SVM Classifier')
plt.show()
