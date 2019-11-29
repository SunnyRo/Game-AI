#k-nearest neightbors
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
data = pd.read_csv("car.data")
# transform data to integer type so we can train
le = preprocessing.LabelEncoder()
## add to a array
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))
predict = "class"
# convert all into 1 list
x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

model = KNeighborsClassifier(n_neighbors=9)
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(accuracy)
predicted = model.predict(x_test)
names = ["unaccuracy", "accuracy", "good", "vgood"]
for x in range(len(x_test)):
    print("predicted: ", predicted[x], "Data: ", x_test[x], "Actual: ", y_test[x], names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)
