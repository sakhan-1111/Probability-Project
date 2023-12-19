########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part IV – Linear Regression Using Python
# 
########################################################################

# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Load dataset from GitHub
url = 'https://raw.githubusercontent.com/sudarshan-koirala/Salary-Prediciton-based-on-Years-of-Experience/master/Salary_Data.csv'

# Create dataframe
df = pd.read_csv(url)

# Define X and y
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

# Create training and testing datasets from X and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instantiate linear regression model
lr = LinearRegression()

# Train linear regression model
lr.fit(X_train, y_train)

# Get prediction from linear regression model
y_pred = lr.predict(X_test)

# Print performance metrices of model
print('Intercept:', lr.intercept_)
print('Coefficients:', lr.coef_)
print('Mean absolute error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean squared error:', metrics.mean_squared_error(y_test, y_pred))
print('Coefficient of determination (R^2 Score):', metrics.r2_score(y_test, y_pred))

plt.figure(figsize=(10, 8))
plt.scatter(X_train, y_train, color = 'green')
plt.plot(X_train, lr.predict(X_train), color = 'purple')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.savefig('4. Salary vs Experience (Training set).png')
plt.savefig('4. Salary vs Experience (Training set).svg')
plt.savefig('4. Salary vs Experience (Training set).jpeg')
plt.savefig('4. Salary vs Experience (Training set).pdf')
plt.clf()

plt.figure(figsize=(10, 8))
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, lr.predict(X_train), color = 'purple')
plt.title('Salary vs Experience (Testing set)')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.savefig('4. Salary vs Experience (Testing set).png')
plt.savefig('4. Salary vs Experience (Testing set).svg')
plt.savefig('4. Salary vs Experience (Testing set).jpeg')
plt.savefig('4. Salary vs Experience (Testing set).pdf')
plt.clf()