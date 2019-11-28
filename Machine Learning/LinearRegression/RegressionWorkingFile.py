import pandas as pd
import numpy as np
## sklearn is machine learning toolkit
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"
# drop G3
x = np.array(data.drop([predict], 1))
# what we want (labeled)
y = np.array(data[predict])
# use machine learning set data, labeled data, then set test_data = 10%
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)
'''
best = 0
for i in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)
    if accuracy > best:
        best = accuracy
        with open("studentmodel.pickle","wb") as f:
            pickle.dump(linear, f)
'''
# load studentmodel.pickle
pickle_in = open("studentmodel.pickle","rb")
linear = pickle.load(pickle_in)
print('Co: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x]);
# matplotlib
# ggplot is style
style.use("ggplot")
temp = "G1"
pyplot.scatter(data[temp], data["G3"])
pyplot.xlabel(temp)
pyplot.ylabel("Final Grade")
pyplot.show()
