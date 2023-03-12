import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_excel("Baseline_ALL_202303.xlsx", sheet_name="ALL")

mycolumns = ["Duration [min]", "Humidity [%]", "Air pressure [mb]", "Water temp. [⁰C]", "Air temp. [⁰C]", "Moon illumination"]
X = df[mycolumns]
Y = df["Symm1"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)
print('Mean squared error:', mse)

print('Predicted values:', Y_pred)
print('Actual values:', Y_test.values)

