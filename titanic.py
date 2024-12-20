import pandas as pd
from sklearn.model_selection import GridSearchCV

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(train.head())
print(train.info())

train['Age']=train['Age'].fillna(test['Age'].mean())
train['Embarked']=train['Embarked'].fillna(test['Embarked'].mode()[0])
train.drop('Cabin',axis=1,inplace=True)
train.drop(['PassengerId','Name'], axis=1, inplace=True)
train['Sex']=train['Sex'].map({'male':0, 'female':1})
train['Embarked']=train['Embarked'].map({'C':0, 'Q': 1, 'S':2})


X_testog = test.copy()

X_testog['Age'] = X_testog['Age'].fillna(X_testog['Age'].mean())
X_testog['Embarked'] = X_testog['Embarked'].fillna(X_testog['Embarked'].mode()[0])
X_testog['Sex'] = X_testog['Sex'].map({'male': 0, 'female': 1})
X_testog['Embarked'] = X_testog['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})


X = train.drop('Survived', axis=1)
y = train['Survived']


from sklearn.model_selection import train_test_split

X = train.drop('Survived', axis=1)  
y = train['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3, min_samples_split=2, min_samples_leaf= 5, random_state=42)

X_train = X_train.drop('Ticket', axis=1)
X_test = X_test.drop('Ticket', axis=1)

print(X_train.info())  
print(X_train.isnull().sum()) 
print(y_train.head())  
print(type(X_train), type(y_train))  

model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Dokładność modelu:", accuracy)

print(classification_report(y_test, y_pred))

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=["Nie przeżył", "Przeżył"], filled=True)
plt.title("Drzewo decyzyjne - Titanic")
plt.show()
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność: {accuracy}")

import matplotlib.pyplot as plt

importance = model.feature_importances_
plt.bar(X_train.columns, importance)
plt.title("Ważność cech")
plt.show()

print(X_train.info())
print(X_train.isnull().sum())
print(y_train.unique())

param_grid = {
    'max_depth': [2, 3, 4, 5, 6, 7, 10],
    'min_samples_split': [ 2, 3, 4, 5, 10],
    'min_samples_leaf': [1, 2, 3, 4,5]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print("Najlepsze parametry:", grid_search.best_params_)
print("Najlepsza dokładność:", grid_search.best_score_)

