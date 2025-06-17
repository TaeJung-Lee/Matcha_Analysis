import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#2024 values, this one is not used anymore due to R^2 being 86 and the new one being 96
# old_values = [75, 77, 100, 97, 96, 94, 99, 97, 96, 85, 90, 100]
# new_values = [37, 38, 50, 45, 47, 47, 50, 48, 47, 45, 45, 51] 

old_values = [69, 77, 85, 84, 79, 79, 81, 84, 73, 67, 63, 67, 75, 77, 100, 97, 96, 94, 99, 97, 96, 85, 90, 100]
new_values = [34, 39, 44, 43, 39, 40, 39, 43, 37, 33, 32, 33, 37, 38, 50, 45, 47, 47, 50, 48, 47, 45, 45, 51] 

#Linear model
x = np.array(new_values).reshape(-1, 1) #converts new_values list into numpy array and reshapes it into a 2D array with one column
y = np.array(old_values)

model = LinearRegression().fit(x, y) #creates linear regression model and fits it to data. Ex: old ≈ slope * new + intercept


#check the goodness of fit with model.score(x, y) to get R^2 to evaluate the regression quality
#I get .899 so about %90 
r_squared = model.score(x, y)
print(f"Model R² (coefficient of determination): {r_squared:.4f}")


#Display model
slope = model.coef_[0] #extracts the learned slope from the model
intercept = model.intercept_
print(f"Linear relationship: old = {slope:.5f} * new + {intercept:.5f}") #5 decimal places 

#2025 new values to convert to old 
new_2025 = [66, 71, 94, 92, 100] #2025-01 to 2025-05 new index values
converted_old = model.predict(np.array(new_2025).reshape(-1, 1))

#2024 new index values to compare to old index values for accuracy/sanity check
sanity_check_new_2024 = [34, 39, 44, 43, 39, 40, 39, 43, 37, 33, 32, 33, 37, 38, 50, 45, 47, 47, 50, 48, 47, 45, 45, 51] #2024-01 to 2024-12
converted_old2 = model.predict(np.array(sanity_check_new_2024).reshape(-1, 1))


#show converted results
print(f"2025 values:")
for i, val in enumerate(converted_old, start=1):
    print(f"2025-{i:02}: {val:.2f}") #final will have 2 decimal places 

print(f"2024 values:")
for i, val in enumerate(converted_old2, start=1):
    print(f"2024-{i:02}: {val:.2f}")



#show graph / scatter plot of the actual data
plt.scatter(new_values, old_values, color='blue', label='Actual Data')

#Regression line
x_line = np.linspace(min(new_values), max(new_values), 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', label=f'Regression Line\nR² = {r_squared:.3f}')

#labels + title
plt.xlabel("New Index Value")
plt.ylabel("Old Index Value")
plt.title("Linear Regression: Mapping New to Old Index Values")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#residuals
residuals = y - model.predict(x) #y are actual values 2024, x are actual values 2024
plt.scatter(x, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("New Index Value")
plt.ylabel("Residuals (Old - Predicted)")
plt.title("Residual Plot")
plt.grid(True)
plt.tight_layout()
plt.show()