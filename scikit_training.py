#mit Python 3 ausfuehren
import numpy as np

training_data = np.loadtxt("/home/pi/git-repos/hello-world/training_data")

x = training_data[:,0:3]
y = training_data[:,3:5]

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor

x_train, x_test, y_train, y_test = train_test_split(x,y)
print("x_train.shape", x_train.shape)
print("y_train.shape", y_train.shape)

reg = MultiOutputRegressor(GradientBoostingRegressor()).fit(x_train, y_train)

print("reg.score(x_train, y_train)", reg.score(x_train, y_train))
print("reg.score(x_test, y_test)", reg.score(x_test, y_test))

output = reg.predict(x_test)