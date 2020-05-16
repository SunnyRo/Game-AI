import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split

# to prevent dont have really large bias number
from sklearn.preprocessing import StandardScaler

# knn tool
from sklearn.neighbors import KNeighborsClassifier

# for testing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("diabetes.csv")
zero_not_accepted = ["Glucose", "BloodPressure", "SkinThickness", "BMI", "Insulin"]
for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0, np.NaN)  # replace 0 with np.NaN nodata
    mean = int(dataset[column].mean(skipna=True))  # find the mean of the dataset
    dataset[column] = dataset[column].replace(
        np.NaN, mean
    )  # replace all np.NaN with the mean value
# split the dataset into train and test
X = dataset.iloc[:, 0:8]  # all row and 0-8 column
y = dataset.iloc[:, 8]  # all row and last column
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)
# feature scaling (scale the data, standerdize data all fit the same scale)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
# using KNN model
# define the model init KNN
classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric="euclidean")
classifier.fit(X_train, y_train)
# Predict the test results
y_pred = classifier.predict(X_test)
confusionMatrix = confusion_matrix(y_test, y_pred)
accuracy = classifier.score(X_test, y_test)
print("Confusion Matrix:")
print(confusionMatrix)
print("Accuracy = {}".format(accuracy))
print("Model predicted total {} people:".format(len(X_test)))
print("Predicted right:")
print("{} people dont have diabetes".format(confusionMatrix[0][0]))
print("{} people have diabetes".format(confusionMatrix[1][1]))
print("Predicted wrong:")
print("{} people have diabetes".format(confusionMatrix[0][1]))
print("{} people dont have diabetes".format(confusionMatrix[1][0]))
