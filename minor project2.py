2) Simple Linear Regression (Sales vs Advertising)

We’ll model the relationship between Advertising Spend and Sales.

  code:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
data = pd.DataFrame({
    'Advertising': [100, 200, 300, 400, 500, 600, 700, 800],
    'Sales': [20, 24, 31, 40, 45, 50, 55, 60]
})

# Split Data
X = data[['Advertising']]
y = data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

# Visualization
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Advertising vs Sales')
plt.xlabel('Advertising Budget')
plt.ylabel('Sales')
plt.show()
