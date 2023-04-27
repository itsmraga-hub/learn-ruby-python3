import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv('MetaAccountUsersTrade1-2023-04-20.csv')
# print(df)

# independent variables
X = df[['id', 'digits', 'trade_mode', 'ticks_bookdepth']]
y = df['spread']  # dependent variables


model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print(predictions)
