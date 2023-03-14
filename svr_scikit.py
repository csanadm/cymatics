import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV #, RandomizedSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


df = pd.read_excel("Baseline_ALL_202303.xlsx", sheet_name="ALL")

mycolumns = ["Duration [min]", "Humidity [%]", "Air pressure [mb]", "Water temp. [⁰C]", "Air temp. [⁰C]", "Moon illumination"]
X = df[mycolumns]
y = df["Symm1"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Define parameter grid for grid search
# C: regularization parameter (fitting well vs overfitting)
# gamma: kernel coefficient (complexity vs generalization)
# epsilon: tube with no penalty
# degree: polynomial degree for 'poly'
# coef0: constant term influence on decision boundary, 'poly' and 'sigmoid'
#param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.01, 0.1, 1], 'epsilon': [0.01, 0.1, 0.5], 'degree': [2, 3, 4], 'coef0': [0.0, 1.0]}
param_grid = {'C': [10, 100], 'gamma': [0.01, 0.1], 'epsilon': [0.01, 0.1], 'degree': [3], 'coef0': [1.0]}

# Fit regression models
#svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1, coef0=1)
#rand_poly = RandomizedSearchCV(SVR(kernel='poly'), param_distributions=param_grid_poly, n_iter=10)
#grid_rbf = GridSearchCV(SVR(kernel='rbf'), param_grid=param_grid)
grid_lin = GridSearchCV(SVR(kernel='linear'), param_grid=param_grid)
grid_poly = GridSearchCV(SVR(kernel='poly'), param_grid=param_grid)
#grid_sig = GridSearchCV(SVR(kernel='sigmoid'), param_grid=param_grid, coef0=1)

# Fit models on training data
#svr_rbf.fit(X_train, y_train)
#svr_lin.fit(X_train, y_train)
#svr_poly.fit(X_train, y_train)
#grid_rbf.fit(X_train, y_train)
grid_lin.fit(X_train, y_train)
grid_poly.fit(X_train, y_train)
#grid_sig.fit(X_train, y_train)


# Print best parameters for each kernel
#print("Best parameters for RBF kernel:", grid_rbf.best_params_)
print("Best parameters for linear kernel:", grid_lin.best_params_)
print("Best parameters for polynomial kernel:", grid_poly.best_params_)
#print("Best parameters for sigmoid kernel:", grid_sig.best_params_)

# Predict on testing data using best parameters
#y_rbf_pred = grid_rbf.predict(X_test)
y_lin_pred = grid_lin.predict(X_test)
y_poly_pred = grid_poly.predict(X_test)
#y_sig_pred = grid_sig.predict(X_test)

# Calculate and print MSE for each model
#mse_rbf = mean_squared_error(y_test, y_rbf_pred)
mse_lin = mean_squared_error(y_test, y_lin_pred)
mse_poly = mean_squared_error(y_test, y_poly_pred)
#mse_sig = mean_squared_error(y_test, y_sig_pred)

#print("MSE for RBF kernel:", mse_rbf)
print("MSE for linear kernel:", mse_lin)
print("MSE for polynomial kernel:", mse_poly)
#print("MSE for sigmoid kernel:", mse_sig)

# Calculate and print MAE for each model
#mae_rbf = mean_absolute_error(y_test, y_rbf_pred)
mae_lin = mean_absolute_error(y_test, y_lin_pred)
mae_poly = mean_absolute_error(y_test, y_poly_pred)
#mae_sig = mean_absolute_error(y_test, y_sig_pred)

#print("MAE for RBF kernel:", mae_rbf)
print("MAE for linear kernel:", mae_lin)
print("MAE for polynomial kernel:", mae_poly)
#print("MAE for sigmoid kernel:", mae_sig)

# Calculate and print R^2 score for each model
#r2_rbf = r2_score(y_test, y_rbf_pred)
r2_lin = r2_score(y_test, y_lin_pred)
r2_poly = r2_score(y_test, y_poly_pred)
#r2_sig = r2_score(y_test, y_sig_pred)

#print("R^2^ score for RBF kernel:", r2_rbf)
print("R^2^ score for linear kernel:", r2_lin)
print("R^2^ score for polynomial kernel:", r2_poly)
#print("R^2^ score for sigmoid kernel:", r2_sig)

# Create scatter plots of actual vs predicted values
plt.figure(figsize=(10,10))
plt.subplot(221) # First subplot in a 4x4 grid
#plt.scatter(y_test,y_rbf_pred) # Scatter plot of actual vs predicted values using RBF kernel 
plt.xlabel('Actual') # X-axis label 
plt.ylabel('Predicted') # Y-axis label 
plt.title('RBF Kernel') # Plot title 

plt.subplot(222) # Second subplot in a 4x4 grid 
plt.scatter(y_test,y_lin_pred) # Scatter plot of actual vs predicted values using linear kernel 
plt.xlabel('Actual') # X-axis label 
plt.ylabel('Predicted') # Y-axis label 
plt.title('Linear Kernel') # Plot title 

plt.subplot(223) # Third subplot in a 4x4 grid 
plt.scatter(y_test,y_poly_pred) # Scatter plot of actual vs predicted values using polynomial kernel 
plt.xlabel('Actual') # X-axis label 
plt.ylabel('Predicted') # Y-axis label 
plt.title('Polynomial Kernel') # Plot title 

plt.subplot(224) # Fourth subplot in a 4x4 grid 
#plt.scatter(y_test,y_sig_pred) # Scatter plot of actual vs predicted values using sigmoid kernel 
plt.xlabel('Actual') # X-axis label 
plt.ylabel('Predicted') # Y-axis label 
plt.title('Sigmoid Kernel') # Plot title 

# Adjust spacing between subplots
plt.tight_layout()

# Save plots
plt.savefig("svr_scikit.png")

