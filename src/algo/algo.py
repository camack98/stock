import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score

def calc_30_day_avg(df):
    df = df.tail(30)
    return df.close.mean()

def logistic_regression(df, df_test):
    df = df.close.to_frame()
    for lag in range(0, 25):
        df[f'lag_{lag}'] = df['close'].shift(lag)
    df.drop(columns='close', inplace=True)

    df['next'] = df['lag_0'].shift(-1)
    df['buy'] = 1
    df.loc[df['next'] < df['lag_0'], 'buy'] = 0
    df = df.dropna(axis=0)
    x_train = df.iloc[:, :25]
    x_train = x_train.reset_index(drop=True)
    y_train = df['buy'].to_frame()
    y_train = y_train.reset_index(drop=True)
    model = LogisticRegression(solver="liblinear")
    model.fit(x_train, y_train)

    df_test = df_test.close.to_frame()
    for lag in range(0, 25):
        df_test[f'lag_{lag}'] = df_test['close'].shift(lag)
    df_test.drop(columns='close', inplace=True)
    df_test = df_test.tail(1)
    prediction = model.predict(df_test)[0]


    # return x_train,y_train,df_test, prediction

    return prediction

