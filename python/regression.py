import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 🚀 Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 🚀 Train Regression Model (Predict Sepal Length based on other features)
X = df
y = iris.target

# 🚀 Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🚀 Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 🚀 Print Coefficients
print("Regression Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)