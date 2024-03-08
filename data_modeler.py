from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Ml Coding Challenge: Design a DataModeler class (in less than 2 hours) which can prepare data, impute missing values,
# fit an ML model and then return predictions for the given train and test toy datasets 


class DataModeler:
    
    def __init__(self, sample_df: pd.DataFrame):
        '''
        Initialize the DataModeler as necessary.
        '''

        self.sample_df = sample_df


    def prepare_data(self, oos_df: pd.DataFrame = None) -> pd.DataFrame:
        '''
        Prepare a dataframe so it contains only the columns to model and having suitable types.
        If the argument is None, work on the training data passed in the constructor.
        '''

        self.oos_df = oos_df if oos_df is not None else self.sample_df.copy()

        # Drop feature: customer id
        self.oos_df.drop(['customer_id'], axis=1, inplace=True)

        # Convert Pandas Column to DateTime
        self.oos_df['transaction_date'] = pd.to_datetime(self.oos_df['transaction_date'], format='%Y-%m-%d')

        # Add a new column to the DataFrame containing only the month of the transaction
        self.oos_df['transaction_month'] = self.oos_df['transaction_date'].dt.month

        # Cyclic Feature Encoding
        self.oos_df['transaction_month_sin'] = np.sin(2 * np.pi * self.oos_df['transaction_month']/12)
        self.oos_df['transaction_month_cos'] = np.cos(2 * np.pi * self.oos_df['transaction_month']/12)

        # Drop Features: 'transaction_date', 'transaction_month'
        self.oos_df.drop(['transaction_date', 'transaction_month'], axis=1, inplace=True)

        return self.oos_df


    def impute_missing(self, oos_df: pd.DataFrame = None) -> pd.DataFrame:
        '''
        Fill any missing values with the appropriate mean (average) value.
        If the argument is None, work on the training data passed in the constructor.
        Hint: Watch out for data leakage in your solution.
        '''

        self.oss_df = oos_df if oos_df is not None else self.oos_df
        columns_with_na = ['amount', 'transaction_month_sin', 'transaction_month_cos']
        for column in columns_with_na :
            self.oos_df[column].fillna(self.oos_df[column].mean(), inplace = True)

        return self.oss_df


    def fit(self) -> None:
        '''
        Fit the model of your choice on the training data paased in the constructor, assuming it has
        been prepared by the functions prepare_data and impute_missing
        '''

        self.X_train = self.oos_df[['amount', 'transaction_month_sin', 'transaction_month_cos']]
        self.y_train = self.oos_df['outcome']
        self.clf = RandomForestClassifier(random_state=42)
        self.clf.fit(self.X_train, self.y_train)


    def model_summary(self) -> str:
        '''
        Create a short summary of the model you have fit.
        '''

        self.y_pred = self.clf.predict(self.X_train)
        acc_train = accuracy_score(self.y_pred, self.y_train)
        print(f"Accuracy : {acc_train}\n")


    def predict(self, oos_df: pd.DataFrame = None) -> pd.Series[bool]:
        '''
        Make a set of predictions with your model. Assume the data has been prepared by the
        functions prepare_data and impute_missing.
        If the argument is None, work on the training data passed in the constructor.
        '''

        self.oos_df = oos_df
        self.X_test = self.oos_df[['amount', 'transaction_month_sin', 'transaction_month_cos']]
        self.predictions = self.clf.predict(self.X_test)
        
        return self.predictions


    def save(self, path: str) -> None:
        '''
        Save the DataModeler so it can be re-used.
        '''

        with open(path, 'wb') as f:
            pickle.dump(self, f)


    @staticmethod
    def load(path: str) -> DataModeler:
        '''
        Reload the DataModeler from the saved state so it can be re-used.
        '''

        with open(path, 'rb') as f:
            return pickle.load(f)


##############################################################
        
# Loading pandas dataframes
transact_train_sample = pd.DataFrame({
    "customer_id": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "amount": [1, 3, 12, 6, 0.5, 0.2, np.nan, 5, np.nan, 3],
    "transaction_date": [
        '2022-01-01', '2022-08-01', None, '2022-12-01', '2022-02-01', None,
        '2022-02-01', '2022-01-01', '2022-11-01', '2022-01-01'
    ],
    "outcome":
    [False, True, True, True, False, False, True, True, True, False]
})

transact_test_sample = pd.DataFrame(
    {
        "customer_id": [21, 22, 23, 24, 25],
        "amount": [0.5, np.nan, 8, 3, 2],
        "transaction_date": [
            '2022-02-01',
            '2022-11-01',
            '2022-06-01',
            None,
            '2022-02-01'
        ]
    }
)

dm = DataModeler(sample_df=transact_train_sample)
print(dm.sample_df.dtypes)

# Data Preparation
dm.prepare_data(dm.sample_df)
print(dm.oos_df)
print(dm.oos_df.dtypes)

# Missing value imputations
dm.impute_missing(dm.oos_df)
print(dm.oos_df)

# Fitting the model
dm.fit()

# Model Summary on Train Set
acc = dm.model_summary()

# Prepare a Test Sample and impute missing values
dm2 = DataModeler(sample_df=transact_test_sample)
print(dm2.sample_df.dtypes)

dm2.prepare_data(dm2.sample_df)
print(dm2.oos_df.dtypes)

adjusted_test_sample = dm2.impute_missing(dm2.oos_df)
print(adjusted_test_sample)

# Prediction on Test Set
predictions = dm.predict(adjusted_test_sample)
print(predictions)

# Saving
dm.save("./datamodeler.pkl")

# Reloading the DataModeler
datamodeler = dm.load("./datamodeler.pkl")

# Let's check the predictions again
print(datamodeler.predictions)

