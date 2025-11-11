3) Data Cleaning & Feature Engineering (Titanic Dataset)

code:

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Check for missing data
print(data.isnull().sum())

# Fill missing values
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Drop irrelevant columns
data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Convert categorical to numeric
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)

# Final cleaned dataset
print(data.head())
