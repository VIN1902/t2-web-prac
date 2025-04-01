import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sample_data.csv")

df = df.dropna() 
df["Age"].fillna(df["Age"].mean(), inplace=True) 
df = df.drop_duplicates() 

# 🚀 Train Regression Model (Predict Salary based on Experience)
X = df[['Experience (Years)']]  # Independent variable
y = df['Salary']  # Dependent variable

model = LinearRegression()
model.fit(X, y)

print("Regression Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

y_pred = model.predict(X_test)
