import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import model_selection
from scipy.stats import chi2_contingency
from sklearn import feature_selection
import os
import datetime

path = 'C:\\Users\\scott\\PycharmProjects\\Funding_Circle'
feature_df = pd.read_csv(os.path.join(path, 'feature_df.csv')) #'loan_data_2007_2014.csv'
#target_df = pd.read_csv(os.path.join(path, 'target_df.csv'))

# # create a new column based on the loan_status column that will be our target variable
# df['good_bad'] = np.where(df.loc[:, 'loan_status'].isin(['Charged Off', 'Default',
#                                                                        'Late (31-120 days)',
#                                                                        'Does not meet the credit policy. Status:Charged Off']),
#                                  0, 1)
# Drop the original 'loan_status' column
#df.drop(columns = ['loan_status'], inplace = True)

# #define feature and taget df to check object features against target variable. Will redefine later.
# feature_df = df.drop('good_bad', axis = 1)
# target_df = df['good_bad']

# # separate object and numerical columns
# df_num = feature_df.select_dtypes(include=[np.number])
# df_cat = feature_df.select_dtypes(include=[np.object])

def woe_ordered_continuous(df, continuous_variabe_name, y_df):
    df = pd.concat([df.groupby(df.columns.values[0], as_index = False)[df.columns.values[1]].count(),
                    df.groupby(df.columns.values[0], as_index = False)[df.columns.values[1]].mean()], axis = 1)
    df = df.iloc[:, [0, 1, 3]]

woe_ordered_continuous(feature_df, 'dti', 'y_df')

#calc woe for each feature
feature_df.groupby(feature_df.columns.values[0], as_index = False)[feature_df.columns.values[1]].count()
    #, df.groupby(df.columns.values[0], as_index = False)[df.columns.values[1]].mean()], axis = 1)




print()