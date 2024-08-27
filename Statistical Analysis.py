import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

#loading data
dfrm = pd.read_csv('projects_data.csv')
dfnm = dfrm.select_dtypes(include='number')

sumry = dfnm.describe()
print(sumry)

print(dfnm.isnull())

skw = dfnm.skew()
krts = dfnm.kurt()
print("\n Skewness of the Distribution: \n\n", skw)
print("\n Kurtosis of the Distribution: \n\n",krts)

X = dfnm.drop(columns=['Design Revision Count','Team Size'])
y = dfnm['Cost Efficiency (%)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rsquare = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-Squared: {rsquare}')

feat_coef = pd.DataFrame({'Feature': X_train.columns, 'Coefficient': model.coef_})
print(feat_coef)

#Cross-Validation
cvscores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f'Cross-Validation R-Squared Scores: {cvscores}')
print(f'Average R-Squared: {np.mean(cvscores)}')


# Residual Analysis 
residuals = y_test - y_pred
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# Histogram of residuals
sns.histplot(residuals, kde=True)
plt.title('Distribution of Residuals')
plt.show()

