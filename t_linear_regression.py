from sklearn.linear_model import LinearRegression

lr = LinearRegression()

X = [
    ['adfasdfasdf', 2],
    ['tretergsdfg', 3],
    ['ewrqwrfffda', 6]
]

Y = [
    [1],
    [2],
    [1]
]
lr.fit(X,Y)
print(lr.predict([['fadsff',2]]))