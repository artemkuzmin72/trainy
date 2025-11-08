# import libs
import numpy as np 
import pandas as pd 
import seaborn as sns
import os
from dotenv import load_dotenv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

load_dotenv()
# read data
data = pd.read_csv(os.getenv('CANCER_DATA_PATH'))
print(data.head())

#drop null columns
data.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
print(data.head())

# map diagnosis to nums
data.diagnosis = [1 if value == "M" else 0 for value in data['diagnosis']]
print(data.head())

# visualize data
plot = data['diagnosis'].value_counts().plot(kind='bar')

# split data
Y = data['diagnosis']
X = data.drop(['diagnosis'], axis=1)
X.head()

# scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.30, random_state=42)
lr = LogisticRegression()

# Train the model on the training data
lr.fit(X_train, y_train)

# Predict the target variable on the test data
y_pred = lr.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# show classification report and confusion matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))