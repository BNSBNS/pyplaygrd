from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC,SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

import sys
from tqdm import tqdm
tqdm.pandas()

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


import sqlite3 as db

pd.pandas.set_option('display.max_columns',None)
print(sys.version, sys.platform, sys.executable)

conn = db.connect('../data/news_popularity.db')

cursor = conn.cursor()
cursor.execute("SELECT name from sqlite_master WHERE type='table';")

print(cursor.fetchall())
cursor.close()

df_articles = pd.read_sql_query('select * from articles',conn)
df_description = pd.read_sql_query('select * from description', conn)
df_keywords = pd.read_sql_query('select * from keywords',conn)

print('shape of articles',df_articles.shape)
print('shape of description', df_description.shape)
print('shape of keywords', df_keywords.shape)

df_premerge = pd.merge(df_keywords, df_description,  on="ID",how="outer")
df_merged = pd.merge(df_premerge, df_articles, on="ID",how="outer")


df_merge_clean = df_merged.dropna().copy()

df_merge_clean['data_channel'].replace(to_replace = [np.nan,'entertainment', 'business','technology','lifestyle','world', 'social_media'], value=[0,1,2,3,4,5,6], inplace=True)
df_merge_clean.replace(to_replace = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'], value=[1,2,3,4,5,6,7], inplace=True)


df_new = df_merge_clean.sample(n=10000, random_state=42).copy()


x_train, x_test, y_train, y_test = train_test_split(df_new.drop(['url'],axis=1), df_new['shares'], test_size=0.3, random_state=42)

models = [LogisticRegression(),
         LinearSVC(),
          SVC(kernel='rbf'),
         KNeighborsClassifier(),
         RandomForestClassifier(),
         DecisionTreeClassifier(),
         GradientBoostingClassifier(),
         GaussianNB()]

model_names = ['LogisticRegression', 'LinearSVM','rbfSVM', 'KNearestNeighbors', 'RandomForestClassifier', 'DecisionTree',
              'GradientBoostingClassifier', 'GaussianNB']

acc = []
eval_acc = {}

for model in tqdm(range(len(models))):
  #  print('1')
    classification_model = models[model]
  #  print('2')
    classification_model.fit(x_train,y_train)
   # print('3')
    pred = classification_model.predict(x_test)
    #print('4')
    acc.append(accuracy_score(pred,y_test))
    #print('5')

eval_acc =  {'Modelling Algo': model_names, 'Accuracy':acc}
print(eval_acc)

acc_table = pd.DataFrame(eval_acc)

print(acc_table)